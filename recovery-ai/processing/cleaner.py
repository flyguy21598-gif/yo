from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from utils.config import get_config

TERM_WEIGHTS = {
    "entropy": 2.0,
    "seed": 1.8,
    "mnemonic": 2.2,
    "checksum": 2.0,
    "wif": 2.1,
    "sha256": 2.1,
    "wallet": 1.5,
    "pattern": 1.4,
    "recovery": 1.6,
    "backup": 1.2,
}

WIF_RE = re.compile(r"\b[5KL][1-9A-HJ-NP-Za-km-z]{50,51}\b")
SHA256_RE = re.compile(r"\b[a-fA-F0-9]{64}\b")
MNEMONIC_HINT_RE = re.compile(r"\b(word|phrase|mnemonic|bip39)\b", flags=re.IGNORECASE)


def normalize_text(text: str) -> str:
    compact = re.sub(r"\s+", " ", text)
    return compact.strip()


def language_score(text: str) -> float:
    ascii_chars = sum(1 for char in text if ord(char) < 128)
    return ascii_chars / max(1, len(text))


def keyword_score(text: str) -> float:
    lowered = text.lower()
    return sum(weight for token, weight in TERM_WEIGHTS.items() if token in lowered)


def pattern_score(text: str) -> float:
    score = 0.0
    if WIF_RE.search(text):
        score += 3.0
    if SHA256_RE.search(text):
        score += 2.5
    if MNEMONIC_HINT_RE.search(text):
        score += 1.0
    return score


def recovery_score(text: str) -> float:
    return keyword_score(text) + pattern_score(text) + (0.5 * language_score(text))


def clean_jsonl(input_path: Path, output_path: Path, min_score: float = 2.5) -> int:
    kept = 0
    with input_path.open("r", encoding="utf-8") as source, output_path.open("w", encoding="utf-8") as sink:
        for line in source:
            record = json.loads(line)
            normalized = normalize_text(str(record.get("text", "")))
            score = recovery_score(normalized)
            if score < min_score:
                continue
            record["text"] = normalized
            record["cleaning"] = {
                "keyword_score": round(keyword_score(normalized), 4),
                "pattern_score": round(pattern_score(normalized), 4),
                "language_score": round(language_score(normalized), 4),
                "recovery_score": round(score, 4),
            }
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            kept += 1
    return kept


def main() -> None:
    parser = argparse.ArgumentParser(description="Score and filter scraped text for recovery relevance.")
    parser.add_argument("input", nargs="?", default="recovery-ai/data/raw/scraped.jsonl")
    parser.add_argument("--output", default=None)
    parser.add_argument("--min-score", type=float, default=2.5)
    args = parser.parse_args()

    config = get_config()
    output = Path(args.output) if args.output else config.cleaned_dir / "cleaned.jsonl"
    kept = clean_jsonl(Path(args.input), output, min_score=args.min_score)
    print(f"kept {kept} cleaned records in {output}")


if __name__ == "__main__":
    main()

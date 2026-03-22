from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from utils.config import get_config

RECOVERY_TERMS = {
    "entropy", "seed", "mnemonic", "checksum", "wif", "sha256", "wallet", "pattern", "recovery", "backup"
}


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_recovery_relevant(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in RECOVERY_TERMS)


def clean_jsonl(input_path: Path, output_path: Path) -> int:
    kept = 0
    with input_path.open("r", encoding="utf-8") as source, output_path.open("w", encoding="utf-8") as sink:
        for line in source:
            record = json.loads(line)
            text = normalize_text(record.get("text", ""))
            if not is_recovery_relevant(text):
                continue
            record["text"] = text
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            kept += 1
    return kept


def main() -> None:
    parser = argparse.ArgumentParser(description="Filter scraped text down to recovery-relevant content.")
    parser.add_argument("input", nargs="?", default="recovery-ai/data/raw/scraped.jsonl")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    config = get_config()
    output = Path(args.output) if args.output else config.cleaned_dir / "cleaned.jsonl"
    kept = clean_jsonl(Path(args.input), output)
    print(f"kept {kept} cleaned records in {output}")


if __name__ == "__main__":
    main()

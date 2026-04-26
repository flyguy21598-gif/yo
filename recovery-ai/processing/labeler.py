from __future__ import annotations

import argparse
import json
from pathlib import Path

from utils.config import get_config

SIGNAL_KEYWORDS = {
    "entropy": {"entropy", "random", "mnemonic", "seed", "checksum", "wif", "sha256", "bip39"},
    "pattern": {"pattern", "transcription", "substitution", "keyboard", "typo", "repeat", "swap"},
    "logic": {"logic", "reason", "because", "therefore", "checksum", "version", "network", "path"},
}


def keyword_vote(text: str, label: str) -> int:
    lowered = text.lower()
    return int(any(keyword in lowered for keyword in SIGNAL_KEYWORDS[label]))


def numeric_vote(text: str, label: str) -> int:
    lowered = text.lower()
    if label == "entropy":
        return int(any(token in lowered for token in ("sha256", "wif", "checksum")))
    if label == "pattern":
        return int(any(token in lowered for token in ("swap", "typo", "replace", "transcription")))
    return int(any(token in lowered for token in ("because", "therefore", "path", "network", "version")))


def rule_vote(text: str, label: str) -> int:
    lowered = text.lower()
    if label == "entropy":
        return int("mnemonic" in lowered and "seed" in lowered)
    if label == "pattern":
        return int("0/o" in lowered or "l/1" in lowered)
    return int("checksum" in lowered and "prefix" in lowered)


def infer_label_with_confidence(text: str, label: str) -> tuple[int, float, dict[str, int]]:
    votes = {
        "keyword": keyword_vote(text, label),
        "numeric": numeric_vote(text, label),
        "rule": rule_vote(text, label),
    }
    total_votes = sum(votes.values())
    label_value = int(total_votes >= 2)
    confidence = total_votes / len(votes)
    return label_value, confidence, votes


def infer_labels(text: str) -> dict[str, dict[str, object]]:
    labels: dict[str, dict[str, object]] = {}
    for signal in ("entropy", "pattern", "logic"):
        value, confidence, provenance = infer_label_with_confidence(text, signal)
        labels[signal] = {
            "value": value,
            "confidence": round(confidence, 4),
            "provenance": provenance,
        }
    return labels


def label_file(input_path: Path, output_path: Path) -> int:
    count = 0
    with input_path.open("r", encoding="utf-8") as source, output_path.open("w", encoding="utf-8") as sink:
        for line in source:
            record = json.loads(line)
            record["labels"] = infer_labels(str(record.get("text", "")))
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Weak-supervision labeler for entropy/pattern/logic signals.")
    parser.add_argument("input", nargs="?", default="recovery-ai/data/cleaned/cleaned.jsonl")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    config = get_config()
    output = Path(args.output) if args.output else config.labeled_dir / "labeled.jsonl"
    count = label_file(Path(args.input), output)
    print(f"labeled {count} records into {output}")


if __name__ == "__main__":
    main()

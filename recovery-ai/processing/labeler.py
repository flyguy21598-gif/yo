from __future__ import annotations

import argparse
import json
from pathlib import Path

from utils.config import get_config


SIGNAL_KEYWORDS = {
    "entropy": {"entropy", "random", "mnemonic", "seed", "checksum", "wif", "sha256"},
    "pattern": {"pattern", "transcription", "substitution", "keyboard", "typo", "repeat"},
    "logic": {"logic", "reason", "because", "therefore", "checksum", "version", "network"},
}


def infer_labels(text: str) -> dict[str, int]:
    lowered = text.lower()
    return {
        label: int(any(keyword in lowered for keyword in keywords))
        for label, keywords in SIGNAL_KEYWORDS.items()
    }


def label_file(input_path: Path, output_path: Path) -> int:
    count = 0
    with input_path.open("r", encoding="utf-8") as source, output_path.open("w", encoding="utf-8") as sink:
        for line in source:
            record = json.loads(line)
            record["labels"] = infer_labels(record.get("text", ""))
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Assign entropy, pattern, and logic signal labels.")
    parser.add_argument("input", nargs="?", default="recovery-ai/data/cleaned/cleaned.jsonl")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    config = get_config()
    output = Path(args.output) if args.output else config.labeled_dir / "labeled.jsonl"
    count = label_file(Path(args.input), output)
    print(f"labeled {count} records into {output}")


if __name__ == "__main__":
    main()

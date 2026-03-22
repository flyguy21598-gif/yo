from __future__ import annotations

import argparse
import json
from pathlib import Path

import trafilatura

from utils.config import get_config


def scrape_archive(input_dir: Path, output_file: Path) -> int:
    count = 0
    with output_file.open("w", encoding="utf-8") as handle:
        for path in sorted(input_dir.rglob("*")):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            extracted = trafilatura.extract(text, include_comments=False, include_tables=False) or text
            handle.write(json.dumps({"source": path.name, "kind": "archive", "text": extracted.strip()}) + "\n")
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract plaintext from archived HTML or raw text snapshots.")
    parser.add_argument("input_dir", nargs="?", default="recovery-ai/data/raw")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    config = get_config()
    output = Path(args.output) if args.output else config.raw_dir / "archive_scraped.jsonl"
    count = scrape_archive(Path(args.input_dir), output)
    print(f"archived {count} files into {output}")


if __name__ == "__main__":
    main()

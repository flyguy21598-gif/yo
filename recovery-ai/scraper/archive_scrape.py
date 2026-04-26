from __future__ import annotations

import argparse
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path

import trafilatura

from utils.config import get_config


def normalize_and_hash(text: str) -> tuple[str, str]:
    cleaned = text.strip()
    digest = hashlib.sha256(cleaned.encode("utf-8", errors="ignore")).hexdigest()
    return cleaned, digest


def scrape_archive(input_dir: Path, output_file: Path) -> int:
    count = 0
    with output_file.open("w", encoding="utf-8") as handle:
        for path in sorted(input_dir.rglob("*")):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            extracted = trafilatura.extract(text, include_comments=False, include_tables=False) or text
            cleaned, digest = normalize_and_hash(extracted)
            row = {
                "source_id": "archive",
                "kind": "archive",
                "location": str(path),
                "ingested_at": datetime.now(tz=UTC).isoformat(),
                "content_hash": digest,
                "text": cleaned,
            }
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract plaintext from archived HTML or raw text snapshots.")
    parser.add_argument("input_dir", nargs="?", default="recovery-ai/data/raw/archives")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    config = get_config()
    output = Path(args.output) if args.output else config.raw_dir / "archive_scraped.jsonl"
    count = scrape_archive(Path(args.input_dir), output)
    print(f"archived {count} files into {output}")


if __name__ == "__main__":
    main()

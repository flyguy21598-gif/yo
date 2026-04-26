from __future__ import annotations

import argparse
from collections.abc import Iterable
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path

import requests
import trafilatura

from scraper.sources import Source, load_sources
from utils.config import get_config


def fetch_url(url: str, timeout: int = 20) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    extracted = trafilatura.extract(response.text, include_comments=False, include_tables=False)
    return extracted or response.text


def read_local(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()


def ingest_source(source: Source) -> list[dict[str, object]]:
    if source.kind == "url":
        text = fetch_url(source.location)
        return [text_record(source, source.location, text)]
    if source.kind == "local_file":
        text = read_local(Path(source.location))
        return [text_record(source, source.location, text)]
    if source.kind == "local_dir":
        rows: list[dict[str, object]] = []
        for path in sorted(Path(source.location).rglob("*")):
            if path.is_file():
                rows.append(text_record(source, str(path), read_local(path)))
        return rows
    raise ValueError(f"unsupported source kind: {source.kind}")


def text_record(source: Source, location: str, text: str) -> dict[str, object]:
    normalized = text.strip()
    digest = content_hash(normalized)
    return {
        "source_id": source.source_id,
        "kind": source.kind,
        "location": location,
        "trust_score": source.trust_score,
        "tags": list(source.tags),
        "ingested_at": datetime.now(tz=UTC).isoformat(),
        "content_hash": digest,
        "text": normalized,
    }


def dedupe_records(records: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    unique: dict[str, dict[str, object]] = {}
    for record in records:
        unique[str(record["content_hash"])] = record
    return list(unique.values())


def write_jsonl(records: list[dict[str, object]], output: Path) -> None:
    with output.open("w", encoding="utf-8") as handle:
        for row in records:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def bootstrap_seed(config_file: Path) -> None:
    if config_file.exists():
        return
    config_file.write_text(
        "Entropy note: wallet backups often include partial phrases and checksum hints.\n"
        "Pattern note: substitutions such as o/0 and l/1 appear in manual transcription.\n"
        "Logic note: if checksum passes but prefix fails, check version bytes and path logic.\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest configured offline sources into deduplicated JSONL.")
    parser.add_argument("--output", default=None, help="Optional output path. Defaults to data/raw/scraped.jsonl")
    args = parser.parse_args()

    config = get_config()
    bootstrap_seed(config.raw_dir / "local_seed.txt")
    sources = load_sources()

    records: list[dict[str, object]] = []
    for source in sources:
        records.extend(ingest_source(source))

    unique_records = dedupe_records(records)
    output = Path(args.output) if args.output else config.raw_dir / "scraped.jsonl"
    write_jsonl(unique_records, output)
    print(f"wrote {len(unique_records)} deduplicated records to {output}")


if __name__ == "__main__":
    main()

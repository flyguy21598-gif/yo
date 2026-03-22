from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import requests
import trafilatura

from scraper.sources import DEFAULT_SOURCES, Source
from utils.config import get_config


def fetch_url(url: str, timeout: int = 20) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    extracted = trafilatura.extract(response.text, include_comments=False, include_tables=False)
    return extracted or response.text


def read_local(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def scrape_sources(sources: Iterable[Source]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for source in sources:
        if source.kind == "url":
            text = fetch_url(source.location)
        else:
            text = read_local(Path(source.location))
        records.append({"source": source.name, "kind": source.kind, "text": text.strip(), "note": source.note})
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape configured recovery-oriented sources into JSONL.")
    parser.add_argument("--output", default=None, help="Optional output path. Defaults to data/raw/scraped.jsonl")
    args = parser.parse_args()

    config = get_config()
    seed = config.raw_dir / "local_seed.txt"
    if not seed.exists():
        seed.write_text(
            "Entropy note: wallet backups often include partial phrases, typo patterns, and checksum hints.\n"
            "Pattern note: clustered substitutions like o/0 and l/1 commonly appear in manual transcriptions.\n"
            "Logic note: if a checksum matches but prefix fails, inspect network/version bytes.\n",
            encoding="utf-8",
        )

    output = Path(args.output) if args.output else config.raw_dir / "scraped.jsonl"
    records = scrape_sources(DEFAULT_SOURCES)
    with output.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"wrote {len(records)} records to {output}")


if __name__ == "__main__":
    main()

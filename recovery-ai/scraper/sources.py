from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from utils.config import get_config


@dataclass(frozen=True, slots=True)
class Source:
    source_id: str
    kind: str
    location: str
    trust_score: float
    enabled: bool
    tags: tuple[str, ...]


def load_sources() -> list[Source]:
    config = get_config()
    if not config.registry_file.exists():
        raise FileNotFoundError(f"missing source registry: {config.registry_file}")
    records = json.loads(config.registry_file.read_text(encoding="utf-8"))
    sources = [
        Source(
            source_id=record["source_id"],
            kind=record["kind"],
            location=record["location"],
            trust_score=float(record["trust_score"]),
            enabled=bool(record["enabled"]),
            tags=tuple(record.get("tags", [])),
        )
        for record in records
    ]
    return [source for source in sources if source.enabled]

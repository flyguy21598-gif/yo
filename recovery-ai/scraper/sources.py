from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Source:
    name: str
    kind: str
    location: str
    note: str


DEFAULT_SOURCES = [
    Source(
        name="local_seed_corpus",
        kind="local",
        location="recovery-ai/data/raw/local_seed.txt",
        note="Offline bootstrap corpus for recovery-related experimentation.",
    ),
    Source(
        name="example_forum_snapshot",
        kind="url",
        location="https://example.com/forum/archive/recovery-thread",
        note="Demonstrates HTTP scraping path when the operator approves source lists.",
    ),
]

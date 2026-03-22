from __future__ import annotations

from dataclasses import dataclass, field
import logging
from typing import Iterable, Sequence

from temporal_engine._compat import np

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class MemoryState:
    """Holds textual and vector memories associated with a branch or federation."""

    texts: list[str] = field(default_factory=list)
    vectors: list[np.ndarray] = field(default_factory=list)

    def add_text(self, text: str) -> None:
        self.texts.append(text)
        logger.debug("Added text memory: %s", text)

    def add_vector(self, vector: Sequence[float] | np.ndarray) -> None:
        self.vectors.append(np.asarray(vector, dtype=float))
        logger.debug("Added vector memory with shape %s", self.vectors[-1].shape)

    def clone(self) -> "MemoryState":
        return MemoryState(
            texts=list(self.texts),
            vectors=[vector.copy() for vector in self.vectors],
        )

    @classmethod
    def merge_many(cls, memories: Iterable["MemoryState"]) -> "MemoryState":
        merged = cls()
        seen_texts: set[str] = set()
        seen_vectors: set[tuple[float, ...]] = set()
        for memory in memories:
            for text in memory.texts:
                if text not in seen_texts:
                    merged.texts.append(text)
                    seen_texts.add(text)
            for vector in memory.vectors:
                key = tuple(vector)
                if key not in seen_vectors:
                    merged.vectors.append(vector.copy())
                    seen_vectors.add(key)
        logger.debug(
            "Merged memories into %d texts and %d vectors",
            len(merged.texts),
            len(merged.vectors),
        )
        return merged

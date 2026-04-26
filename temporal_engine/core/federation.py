from __future__ import annotations

from dataclasses import dataclass, field
import logging
from typing import Iterable

from temporal_engine._compat import nx

from temporal_engine.core.memory import MemoryState

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class Federation:
    """Represents the unified global state after branch reconciliation."""

    global_graph: nx.Graph = field(default_factory=nx.Graph)
    global_memory: MemoryState = field(default_factory=MemoryState)

    def merge_memories(self, memories: Iterable[MemoryState]) -> MemoryState:
        merged = MemoryState.merge_many(memories)
        logger.debug(
            "Federation merged memory totals: texts=%d vectors=%d",
            len(merged.texts),
            len(merged.vectors),
        )
        return merged

    def consolidate(self, graph: nx.Graph, memory: MemoryState) -> None:
        self.global_graph = graph
        self.global_memory = memory
        logger.info(
            "Federation consolidated state: nodes=%d edges=%d texts=%d vectors=%d",
            self.global_graph.number_of_nodes(),
            self.global_graph.number_of_edges(),
            len(self.global_memory.texts),
            len(self.global_memory.vectors),
        )

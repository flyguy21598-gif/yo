from __future__ import annotations

from dataclasses import dataclass, field
import logging

from temporal_engine._compat import nx, np

from temporal_engine.core.memory import MemoryState
from temporal_engine.core.temporal_branch import TemporalBranch

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class TemporalManager:
    """Creates, tracks, evolves, and cleans up temporal branches."""

    active_branches: dict[str, TemporalBranch] = field(default_factory=dict)
    current_time: int = 0
    _branch_counter: int = 0
    rng: np.random.Generator = field(default_factory=np.random.default_rng, repr=False)

    def fork(self, source_graph: nx.Graph, source_memory: MemoryState | None = None) -> TemporalBranch:
        branch_id = f"branch-{self._branch_counter}"
        self._branch_counter += 1
        branch = TemporalBranch(
            branch_id=branch_id,
            graph=source_graph.copy(as_view=False),
            memory=(source_memory.clone() if source_memory else MemoryState()),
            creation_time=self.current_time,
            rng=np.random.default_rng(int(self.rng.integers(0, 2**31 - 1))),
        )
        self.active_branches[branch_id] = branch
        logger.info("Forked %s at time %d", branch_id, self.current_time)
        return branch

    def tick(self) -> None:
        logger.debug("Tick start: time=%d active=%d", self.current_time, len(self.active_branches))
        self.current_time += 1
        for branch in list(self.active_branches.values()):
            branch.evolve()
        self.cleanup_dead_branches()
        logger.debug("Tick end: time=%d active=%d", self.current_time, len(self.active_branches))

    def cleanup_dead_branches(self) -> None:
        dead_branch_ids = [branch_id for branch_id, branch in self.active_branches.items() if not branch.alive]
        for branch_id in dead_branch_ids:
            del self.active_branches[branch_id]
            logger.info("Cleaned up dead branch %s", branch_id)

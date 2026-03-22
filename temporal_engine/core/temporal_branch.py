from __future__ import annotations

from dataclasses import dataclass, field
import logging

from temporal_engine._compat import nx, np

from temporal_engine.core.memory import MemoryState

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class TemporalBranch:
    """Encapsulates a forked graph state and its lifecycle."""

    branch_id: str
    graph: nx.Graph
    memory: MemoryState = field(default_factory=MemoryState)
    divergence_factor: float = 0.0
    age: int = 0
    creation_time: int = 0
    alive: bool = True
    rng: np.random.Generator = field(default_factory=np.random.default_rng, repr=False)

    def evolve(self) -> None:
        """Apply a random perturbation to the branch graph and memory."""
        if not self.alive:
            logger.debug("Skipping evolution for dead branch %s", self.branch_id)
            return

        self.age += 1
        operation = self.rng.choice(["add_node", "add_edge", "remove_edge", "memory"])
        logger.debug("Evolving branch %s using operation %s", self.branch_id, operation)

        if operation == "add_node":
            new_node = max(self.graph.nodes, default=-1) + 1
            self.graph.add_node(new_node)
            if self.graph.number_of_nodes() > 1:
                partner = int(self.rng.choice(list(n for n in self.graph.nodes if n != new_node)))
                self.graph.add_edge(new_node, partner)
        elif operation == "add_edge":
            nodes = list(self.graph.nodes)
            if len(nodes) < 2:
                self.graph.add_node(0)
                nodes = list(self.graph.nodes)
            source, target = self.rng.choice(nodes, size=2, replace=False)
            self.graph.add_edge(int(source), int(target))
        elif operation == "remove_edge":
            edges = list(self.graph.edges)
            if edges:
                edge_index = int(self.rng.integers(0, len(edges)))
                self.graph.remove_edge(*edges[edge_index])
            else:
                self.graph.add_node(max(self.graph.nodes, default=-1) + 1)
        else:
            vector = self.rng.normal(loc=self.age, scale=0.1, size=3)
            self.memory.add_text(f"branch={self.branch_id};age={self.age}")
            self.memory.add_vector(vector)

        self.divergence_factor += float(self.rng.uniform(0.05, 0.35))
        self._update_lifecycle()
        logger.info(
            "Branch %s evolved: age=%d divergence=%.3f alive=%s",
            self.branch_id,
            self.age,
            self.divergence_factor,
            self.alive,
        )

    def terminate(self) -> None:
        self.alive = False
        logger.info("Branch %s terminated", self.branch_id)

    def _update_lifecycle(self) -> None:
        death_probability = min(0.02 + (0.015 * self.age) + (0.03 * self.divergence_factor), 0.8)
        if float(self.rng.random()) < death_probability:
            self.alive = False
            logger.debug(
                "Branch %s marked dead with probability %.3f",
                self.branch_id,
                death_probability,
            )

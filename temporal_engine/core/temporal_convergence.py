from __future__ import annotations

from dataclasses import dataclass, field
import logging
from typing import Iterable

from temporal_engine._compat import nx, np

from temporal_engine.core.federation import Federation
from temporal_engine.core.temporal_branch import TemporalBranch

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class TemporalConvergence:
    """Reconciles multiple branches into a single federation state."""

    rng: np.random.Generator = field(default_factory=np.random.default_rng, repr=False)

    def reconcile(self, federation: Federation, branches: Iterable[TemporalBranch]) -> nx.Graph:
        branch_list = [branch for branch in branches if branch.alive]
        if not branch_list:
            logger.info("No active branches available for reconciliation")
            return federation.global_graph

        weights = {branch.branch_id: self._weight(branch) for branch in branch_list}
        total_weight = sum(weights.values())
        merged_graph = nx.Graph()

        for branch in branch_list:
            merged_graph.add_nodes_from(branch.graph.nodes(data=True))

        edge_scores: dict[tuple[int, int], float] = {}
        for branch in branch_list:
            for edge in branch.graph.edges:
                normalized_edge = tuple(sorted(edge))
                edge_scores[normalized_edge] = edge_scores.get(normalized_edge, 0.0) + weights[branch.branch_id]

        for edge, score in edge_scores.items():
            probability = min(score / total_weight, 1.0)
            if float(self.rng.random()) <= probability:
                merged_graph.add_edge(*edge)

        merged_memory = federation.merge_memories(branch.memory for branch in branch_list)
        federation.consolidate(merged_graph, merged_memory)
        logger.info(
            "Reconciled %d branches into federation with %d nodes and %d edges",
            len(branch_list),
            merged_graph.number_of_nodes(),
            merged_graph.number_of_edges(),
        )
        return merged_graph

    @staticmethod
    def _weight(branch: TemporalBranch) -> float:
        return max(0.1, (1.0 / (1.0 + branch.divergence_factor)) + (0.05 * branch.age))

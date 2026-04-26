from __future__ import annotations

import logging

from temporal_engine._compat import np

from temporal_engine.core.federation import Federation
from temporal_engine.core.temporal_convergence import TemporalConvergence
from temporal_engine.core.temporal_manager import TemporalManager

logger = logging.getLogger(__name__)


def temporal_evolution_round(
    federation: Federation,
    rounds: int,
    *,
    branches_per_round: int = 2,
    seed: int | None = None,
) -> Federation:
    """Execute a fork -> evolve -> reconcile loop for a given number of rounds."""
    rng = np.random.default_rng(seed)
    manager = TemporalManager(rng=np.random.default_rng(int(rng.integers(0, 2**31 - 1))))
    convergence = TemporalConvergence(rng=np.random.default_rng(int(rng.integers(0, 2**31 - 1))))

    for round_index in range(rounds):
        manager.current_time = round_index
        logger.info("Starting temporal evolution round %d", round_index + 1)
        for _ in range(branches_per_round):
            manager.fork(federation.global_graph, federation.global_memory)
        manager.tick()
        if manager.active_branches:
            convergence.reconcile(federation, manager.active_branches.values())
        else:
            logger.info("All branches expired during round %d", round_index + 1)

    return federation

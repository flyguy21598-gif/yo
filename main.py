from __future__ import annotations

import logging

from temporal_engine._compat import nx

from temporal_engine.core.federation import Federation
from temporal_engine.core.memory import MemoryState
from temporal_engine.simulation.runner import temporal_evolution_round


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def build_initial_federation() -> Federation:
    graph = nx.cycle_graph(4)
    memory = MemoryState(texts=["initial-state"])
    federation = Federation(global_graph=graph, global_memory=memory)
    return federation


def main() -> None:
    configure_logging()
    federation = build_initial_federation()
    result = temporal_evolution_round(federation, rounds=5, branches_per_round=3, seed=42)

    logging.info("Simulation complete")
    logging.info("Global nodes: %s", sorted(result.global_graph.nodes()))
    logging.info("Global edges: %s", sorted(tuple(sorted(edge)) for edge in result.global_graph.edges))
    logging.info("Memories: %s", result.global_memory.texts)


if __name__ == "__main__":
    main()

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import logging
from pathlib import Path
import time

from temporal_engine._compat import nx

from temporal_engine.core.federation import Federation
from temporal_engine.core.memory import MemoryState
from temporal_engine.simulation.runner import temporal_evolution_round

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class BenchmarkResult:
    rounds: int
    branches_per_round: int
    elapsed_seconds: float
    final_nodes: int
    final_edges: int
    final_text_memories: int
    final_vector_memories: int


def run_benchmark(
    *,
    rounds: int = 25,
    branches_per_round: int = 4,
    seed: int = 123,
) -> BenchmarkResult:
    """Run a reproducible performance benchmark for the simulation loop."""
    federation = Federation(
        global_graph=nx.cycle_graph(12),
        global_memory=MemoryState(texts=["benchmark-seed"]),
    )
    started = time.perf_counter()
    temporal_evolution_round(
        federation,
        rounds=rounds,
        branches_per_round=branches_per_round,
        seed=seed,
    )
    elapsed = time.perf_counter() - started

    return BenchmarkResult(
        rounds=rounds,
        branches_per_round=branches_per_round,
        elapsed_seconds=elapsed,
        final_nodes=federation.global_graph.number_of_nodes(),
        final_edges=federation.global_graph.number_of_edges(),
        final_text_memories=len(federation.global_memory.texts),
        final_vector_memories=len(federation.global_memory.vectors),
    )


def write_benchmark_report(result: BenchmarkResult, output_path: str = "benchmark_results.json") -> Path:
    output = Path(output_path)
    output.write_text(json.dumps(asdict(result), indent=2))
    logger.info("Wrote benchmark report to %s", output)
    return output


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    result = run_benchmark()
    report_path = write_benchmark_report(result)
    logger.info("Benchmark result: %s", asdict(result))
    logger.info("Report path: %s", report_path)


if __name__ == "__main__":
    main()

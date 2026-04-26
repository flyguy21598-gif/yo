from temporal_engine._compat import nx

from temporal_engine.benchmark import run_benchmark
from temporal_engine.core.federation import Federation
from temporal_engine.core.memory import MemoryState
from temporal_engine.simulation.runner import temporal_evolution_round


def test_temporal_evolution_round_keeps_progression_across_rounds() -> None:
    federation = Federation(global_graph=nx.cycle_graph(4), global_memory=MemoryState(texts=["seeded"]))
    temporal_evolution_round(federation, rounds=4, branches_per_round=2, seed=99)

    assert federation.global_graph.number_of_nodes() >= 4
    assert federation.global_graph.number_of_edges() >= 1
    assert len(federation.global_memory.texts) >= 1


def test_benchmark_returns_valid_shape() -> None:
    result = run_benchmark(rounds=4, branches_per_round=2, seed=9)

    assert result.rounds == 4
    assert result.branches_per_round == 2
    assert result.elapsed_seconds >= 0.0
    assert result.final_nodes >= 1
    assert result.final_edges >= 0
    assert result.final_text_memories >= 1
    assert result.final_vector_memories >= 0

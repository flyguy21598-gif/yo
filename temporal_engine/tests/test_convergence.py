from temporal_engine._compat import nx

from temporal_engine.core.federation import Federation
from temporal_engine.core.memory import MemoryState
from temporal_engine.core.temporal_branch import TemporalBranch
from temporal_engine.core.temporal_convergence import TemporalConvergence


class AlwaysKeepRNG:
    def random(self, size=None):
        return 0.0


def test_convergence_merges_graphs_and_memories() -> None:
    branch_one_graph = nx.Graph()
    branch_one_graph.add_edge(0, 1)
    branch_two_graph = nx.Graph()
    branch_two_graph.add_edge(1, 2)

    memory_one = MemoryState(texts=["alpha"])
    memory_two = MemoryState(texts=["beta"])

    branch_one = TemporalBranch(
        branch_id="b1",
        graph=branch_one_graph,
        memory=memory_one,
        divergence_factor=0.2,
        age=2,
    )
    branch_two = TemporalBranch(
        branch_id="b2",
        graph=branch_two_graph,
        memory=memory_two,
        divergence_factor=0.1,
        age=1,
    )
    federation = Federation()
    convergence = TemporalConvergence(rng=AlwaysKeepRNG())

    merged_graph = convergence.reconcile(federation, [branch_one, branch_two])

    assert set(merged_graph.nodes) == {0, 1, 2}
    assert set(map(tuple, map(sorted, merged_graph.edges))) == {(0, 1), (1, 2)}
    assert federation.global_graph.number_of_edges() == 2
    assert federation.global_memory.texts == ["alpha", "beta"]


def test_temporal_evolution_round_is_deterministic_with_seed() -> None:
    from temporal_engine.simulation.runner import temporal_evolution_round

    federation_one = Federation(global_graph=nx.cycle_graph(4), global_memory=MemoryState(texts=["seeded"]))
    federation_two = Federation(global_graph=nx.cycle_graph(4), global_memory=MemoryState(texts=["seeded"]))

    result_one = temporal_evolution_round(federation_one, rounds=3, branches_per_round=2, seed=11)
    result_two = temporal_evolution_round(federation_two, rounds=3, branches_per_round=2, seed=11)

    assert sorted(result_one.global_graph.nodes) == sorted(result_two.global_graph.nodes)
    assert sorted(result_one.global_graph.edges) == sorted(result_two.global_graph.edges)
    assert result_one.global_memory.texts == result_two.global_memory.texts

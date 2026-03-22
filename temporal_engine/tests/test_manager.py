from temporal_engine._compat import nx, np

from temporal_engine.core.temporal_manager import TemporalManager


class StableRNG:
    def integers(self, low, high=None, size=None):
        return 7


def test_manager_forks_and_cleans_dead_branches() -> None:
    graph = nx.path_graph(3)
    manager = TemporalManager(rng=StableRNG())

    branch = manager.fork(graph)
    assert branch.branch_id in manager.active_branches
    assert manager.active_branches[branch.branch_id].graph is not graph

    manager.active_branches[branch.branch_id].terminate()
    manager.cleanup_dead_branches()

    assert branch.branch_id not in manager.active_branches

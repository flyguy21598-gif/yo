from temporal_engine._compat import nx, np

from temporal_engine.core.temporal_branch import TemporalBranch


class PredictableRNG:
    def __init__(self) -> None:
        self._choice_calls = 0

    def choice(self, options, size=None, replace=True):
        if isinstance(options, list) and size is None:
            return "memory"
        if size == 2:
            values = list(options)
            return np.array(values[:2])
        return options[0]

    def normal(self, loc=0.0, scale=1.0, size=None):
        return np.ones(size) * loc

    def uniform(self, low=0.0, high=1.0, size=None):
        return 0.2

    def random(self, size=None):
        return 0.99

    def integers(self, low, high=None, size=None):
        return 0


def test_branch_evolves_and_records_memory() -> None:
    graph = nx.Graph()
    graph.add_edge(0, 1)
    branch = TemporalBranch(branch_id="branch-test", graph=graph, rng=PredictableRNG())

    branch.evolve()

    assert branch.age == 1
    assert branch.alive is True
    assert branch.divergence_factor > 0
    assert len(branch.memory.texts) == 1
    assert len(branch.memory.vectors) == 1

from temporal_engine._compat import np

from temporal_engine.core.memory import MemoryState


def test_memory_merge_deduplicates_text_and_vectors() -> None:
    first = MemoryState(texts=["alpha", "beta"], vectors=[np.asarray([1.0, 2.0])])
    second = MemoryState(texts=["beta", "gamma"], vectors=[np.asarray([1.0, 2.0]), np.asarray([3.0, 4.0])])

    merged = MemoryState.merge_many([first, second])

    assert merged.texts == ["alpha", "beta", "gamma"]
    assert len(merged.vectors) == 2

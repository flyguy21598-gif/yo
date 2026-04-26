from __future__ import annotations

from collections.abc import Iterable
from math import log2


def accuracy_score(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    true_list = list(y_true)
    pred_list = list(y_pred)
    if not true_list:
        return 0.0
    matches = sum(int(a == b) for a, b in zip(true_list, pred_list))
    return matches / len(true_list)


def shannon_entropy(text: str) -> float:
    if not text:
        return 0.0
    counts = {char: text.count(char) for char in set(text)}
    total = len(text)
    return -sum((count / total) * log2(count / total) for count in counts.values())


def mean(values: Iterable[float]) -> float:
    data = list(values)
    return sum(data) / len(data) if data else 0.0

from __future__ import annotations


def combine_scores(entropy: float, pattern: float, logic: float) -> float:
    return round((0.45 * entropy) + (0.30 * pattern) + (0.25 * logic), 6)

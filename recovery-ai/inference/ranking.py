from __future__ import annotations


def combine_scores(entropy: float, pattern: float, logic: float) -> float:
    return round((0.45 * entropy) + (0.30 * pattern) + (0.25 * logic), 6)


def confidence_band(score: float) -> str:
    if score >= 0.8:
        return "very_high"
    if score >= 0.6:
        return "high"
    if score >= 0.4:
        return "moderate"
    if score >= 0.2:
        return "low"
    return "very_low"

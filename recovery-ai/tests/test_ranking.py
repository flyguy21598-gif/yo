from __future__ import annotations

from inference.ranking import combine_scores, confidence_band


def test_score_range() -> None:
    score = combine_scores(0.8, 0.6, 0.4)
    assert 0.0 <= score <= 1.0


def test_confidence_band() -> None:
    assert confidence_band(0.81) == "very_high"
    assert confidence_band(0.61) == "high"
    assert confidence_band(0.41) == "moderate"
    assert confidence_band(0.21) == "low"
    assert confidence_band(0.19) == "very_low"

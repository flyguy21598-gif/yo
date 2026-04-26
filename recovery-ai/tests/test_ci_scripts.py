from __future__ import annotations

import json
from pathlib import Path

from scripts.evaluate_candidate import evaluate


def test_evaluate_candidate_passes() -> None:
    metrics = {
        "entropy": {"model": "entropy", "train_rows": 3, "positive_rate": 0.5},
        "pattern": {"model": "pattern", "train_rows": 2, "positive_rate": 0.2},
        "logic": {"model": "logic", "train_rows": 4, "positive_rate": 0.8},
    }
    ok, errors = evaluate(metrics)
    assert ok is True
    assert errors == []


def test_evaluate_candidate_fails() -> None:
    metrics = {
        "entropy": {"model": "entropy", "train_rows": 0, "positive_rate": 1.5},
    }
    ok, errors = evaluate(metrics)
    assert ok is False
    assert len(errors) == 2

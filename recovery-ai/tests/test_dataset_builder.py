from __future__ import annotations

import json
from pathlib import Path

from processing.dataset_builder import build_dataset


def test_build_dataset(tmp_path: Path) -> None:
    input_file = tmp_path / "labeled.jsonl"
    rows = [
        {"text": "a", "content_hash": "1", "labels": {"entropy": {"value": 1}, "pattern": {"value": 0}, "logic": {"value": 0}}},
        {"text": "b", "content_hash": "2", "labels": {"entropy": {"value": 0}, "pattern": {"value": 1}, "logic": {"value": 0}}},
        {"text": "c", "content_hash": "3", "labels": {"entropy": {"value": 0}, "pattern": {"value": 0}, "logic": {"value": 1}}},
    ]
    input_file.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")
    out_dir = tmp_path / "datasets"
    snapshot = build_dataset(input_file, out_dir, seed=7)
    assert (snapshot / "manifest.json").exists()
    assert (snapshot / "train.jsonl").exists()
    assert (snapshot / "val.jsonl").exists()
    assert (snapshot / "test.jsonl").exists()

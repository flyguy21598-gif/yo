from __future__ import annotations

import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from processing.cleaner import clean_jsonl
from processing.dataset_builder import build_dataset
from processing.labeler import label_file


def write_fixture(path: Path) -> None:
    rows = [
        {"source_id": "smoke", "text": "WIF checksum mismatch with 0/O swap and mnemonic seed backup note"},
        {"source_id": "smoke", "text": "General random note without useful context"},
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def main() -> None:
    base = PROJECT_ROOT / "data"
    raw = base / "raw" / "ci_smoke_input.jsonl"
    cleaned = base / "cleaned" / "ci_smoke_cleaned.jsonl"
    labeled = base / "labeled" / "ci_smoke_labeled.jsonl"
    datasets = base / "datasets"

    for directory in (raw.parent, cleaned.parent, labeled.parent, datasets):
        directory.mkdir(parents=True, exist_ok=True)

    write_fixture(raw)
    kept = clean_jsonl(raw, cleaned, min_score=2.5)
    if kept < 1:
        raise RuntimeError("smoke failed: no records passed cleaner")

    labeled_count = label_file(cleaned, labeled)
    if labeled_count < 1:
        raise RuntimeError("smoke failed: no records labeled")

    snapshot = build_dataset(labeled, datasets, seed=42)
    manifest = json.loads((snapshot / "manifest.json").read_text(encoding="utf-8"))
    if manifest["counts"]["test"] < 1:
        raise RuntimeError("smoke failed: test split empty")

    print(json.dumps({"smoke": "pass", "snapshot": snapshot.name, "counts": manifest["counts"]}, indent=2))


if __name__ == "__main__":
    main()

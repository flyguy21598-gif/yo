from __future__ import annotations

import argparse
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
import random

from utils.config import get_config


def dataset_id(rows: list[dict[str, object]]) -> str:
    payload = "\n".join(sorted(str(row.get("content_hash", row.get("text", ""))) for row in rows))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def split_rows(rows: list[dict[str, object]], seed: int) -> dict[str, list[dict[str, object]]]:
    random.Random(seed).shuffle(rows)
    n_total = len(rows)
    n_train = int(n_total * 0.7)
    n_val = int(n_total * 0.15)
    return {
        "train": rows[:n_train],
        "val": rows[n_train : n_train + n_val],
        "test": rows[n_train + n_val :],
    }


def save_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_dataset(input_path: Path, output_dir: Path, seed: int = 42) -> Path:
    rows = [json.loads(line) for line in input_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    did = dataset_id(rows)
    target_dir = output_dir / did
    target_dir.mkdir(parents=True, exist_ok=True)

    splits = split_rows(rows, seed)
    for name, part in splits.items():
        save_jsonl(target_dir / f"{name}.jsonl", part)

    manifest = {
        "dataset_id": did,
        "created_at": datetime.now(tz=UTC).isoformat(),
        "seed": seed,
        "counts": {name: len(rows) for name, rows in splits.items()},
        "input": str(input_path),
    }
    (target_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return target_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Create immutable dataset snapshot and train/val/test manifests.")
    parser.add_argument("input", nargs="?", default="recovery-ai/data/labeled/labeled.jsonl")
    parser.add_argument("--output-dir", default="recovery-ai/data/datasets")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    config = get_config()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    snapshot = build_dataset(Path(args.input), output_dir, seed=args.seed)
    (config.dataset_dir / "LATEST").write_text(snapshot.name, encoding="utf-8")
    print(f"built dataset snapshot: {snapshot}")


if __name__ == "__main__":
    main()

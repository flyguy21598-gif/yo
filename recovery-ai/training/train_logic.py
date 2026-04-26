from __future__ import annotations

import json
from pathlib import Path

from models.logic_model import LogicInferenceModel
from utils.config import get_config


def load_dataset(path: Path) -> tuple[list[str], list[int]]:
    texts, labels = [], []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            texts.append(record["text"])
            labels.append(int(record["labels"]["logic"]["value"]))
    return texts, labels


def latest_train_file(config_path: Path) -> Path:
    dataset_id = config_path.read_text(encoding="utf-8").strip()
    return config_path.parent / dataset_id / "train.jsonl"


def main() -> None:
    config = get_config()
    train_file = latest_train_file(config.dataset_dir / "LATEST")
    texts, labels = load_dataset(train_file)
    model = LogicInferenceModel()
    model.fit(texts, labels)
    output = config.model_dir / "logic.joblib"
    model.save(output)
    metrics = {"model": "logic", "train_rows": len(texts), "positive_rate": round(sum(labels) / max(1, len(labels)), 6)}
    (config.model_dir / "logic.metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(f"saved logic model to {output}")


if __name__ == "__main__":
    main()

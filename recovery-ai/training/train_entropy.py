from __future__ import annotations

import json
from pathlib import Path

from models.entropy_model import EntropyClassifier
from utils.config import get_config


def load_dataset(path: Path) -> tuple[list[str], list[int]]:
    texts, labels = [], []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            texts.append(record["text"])
            labels.append(record["labels"]["entropy"])
    return texts, labels


def main() -> None:
    config = get_config()
    dataset = config.labeled_dir / "labeled.jsonl"
    texts, labels = load_dataset(dataset)
    model = EntropyClassifier()
    model.fit(texts, labels)
    output = config.model_dir / "entropy.joblib"
    model.save(output)
    print(f"saved entropy model to {output}")


if __name__ == "__main__":
    main()

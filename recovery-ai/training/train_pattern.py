from __future__ import annotations

import json
from pathlib import Path

from models.pattern_model import PatternDetector
from utils.config import get_config


def load_dataset(path: Path) -> tuple[list[str], list[int]]:
    texts, labels = [], []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            texts.append(record["text"])
            labels.append(record["labels"]["pattern"])
    return texts, labels


def main() -> None:
    config = get_config()
    dataset = config.labeled_dir / "labeled.jsonl"
    texts, labels = load_dataset(dataset)
    model = PatternDetector()
    model.fit(texts, labels)
    output = config.model_dir / "pattern.joblib"
    model.save(output)
    print(f"saved pattern model to {output}")


if __name__ == "__main__":
    main()

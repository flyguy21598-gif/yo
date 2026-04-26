from __future__ import annotations

import json
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from models.unified_model import MultiHeadRecoveryNet, UnifiedModelBundle
from processing.tokenizer import RecoveryTokenizer
from utils.config import get_config


def load_dataset(path: Path):
    texts, labels = [], []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            texts.append(record["text"])
            labels.append([
                int(record["labels"]["entropy"]["value"]),
                int(record["labels"]["pattern"]["value"]),
                int(record["labels"]["logic"]["value"]),
            ])
    return texts, torch.tensor(labels, dtype=torch.float32)


def latest_train_file(config_path: Path) -> Path:
    dataset_id = config_path.read_text(encoding="utf-8").strip()
    return config_path.parent / dataset_id / "train.jsonl"


def main() -> None:
    config = get_config()
    texts, targets = load_dataset(latest_train_file(config.dataset_dir / "LATEST"))
    tokenizer = RecoveryTokenizer(max_features=config.max_features)
    features = tokenizer.fit_transform(texts)
    dense_features = torch.tensor(features.toarray(), dtype=torch.float32)

    dataset = TensorDataset(dense_features, targets)
    loader = DataLoader(dataset, batch_size=config.batch_size, shuffle=True)

    model = MultiHeadRecoveryNet(input_dim=dense_features.shape[1])
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.BCELoss()

    for _ in range(config.epochs):
        for batch_x, batch_y in loader:
            optimizer.zero_grad()
            outputs = model(batch_x)
            stacked = torch.cat([outputs["entropy"], outputs["pattern"], outputs["logic"]], dim=1)
            loss = loss_fn(stacked, batch_y)
            loss.backward()
            optimizer.step()

    torch.save(tokenizer.vectorizer, config.model_dir / "unified_vectorizer.pt")
    UnifiedModelBundle(model=model).save(config.model_dir / "unified.pt")
    summary = {
        "model": "unified",
        "train_rows": len(texts),
        "input_dim": int(dense_features.shape[1]),
        "epochs": config.epochs,
        "batch_size": config.batch_size,
    }
    (config.model_dir / "unified.metrics.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"saved unified model bundle to {config.model_dir}")


if __name__ == "__main__":
    main()

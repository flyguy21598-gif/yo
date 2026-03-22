from __future__ import annotations

import json
from pathlib import Path

import torch
from torch import nn

from models.unified_model import MultiHeadRecoveryNet, UnifiedModelBundle
from processing.tokenizer import RecoveryTokenizer
from utils.config import get_config


def load_dataset(path: Path):
    texts, labels = [], []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            texts.append(record["text"])
            labels.append([record["labels"][key] for key in ("entropy", "pattern", "logic")])
    return texts, torch.tensor(labels, dtype=torch.float32)


def main() -> None:
    config = get_config()
    texts, targets = load_dataset(config.labeled_dir / "labeled.jsonl")
    tokenizer = RecoveryTokenizer(max_features=config.max_features)
    features = tokenizer.fit_transform(texts)
    inputs = torch.tensor(features.toarray(), dtype=torch.float32)

    model = MultiHeadRecoveryNet(input_dim=inputs.shape[1])
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.BCELoss()

    for _ in range(config.epochs):
        optimizer.zero_grad()
        outputs = model(inputs)
        stacked = torch.cat([outputs["entropy"], outputs["pattern"], outputs["logic"]], dim=1)
        loss = loss_fn(stacked, targets)
        loss.backward()
        optimizer.step()

    torch.save(tokenizer.vectorizer, config.model_dir / "unified_vectorizer.pt")
    UnifiedModelBundle(model=model).save(config.model_dir / "unified.pt")
    print(f"saved unified model bundle to {config.model_dir}")


if __name__ == "__main__":
    main()

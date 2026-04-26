from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import torch
from torch import nn


class MultiHeadRecoveryNet(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 128) -> None:
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
        )
        self.entropy_head = nn.Linear(hidden_dim, 1)
        self.pattern_head = nn.Linear(hidden_dim, 1)
        self.logic_head = nn.Linear(hidden_dim, 1)

    def forward(self, inputs: torch.Tensor) -> dict[str, torch.Tensor]:
        shared = self.encoder(inputs)
        return {
            "entropy": torch.sigmoid(self.entropy_head(shared)),
            "pattern": torch.sigmoid(self.pattern_head(shared)),
            "logic": torch.sigmoid(self.logic_head(shared)),
        }


@dataclass
class UnifiedModelBundle:
    model: MultiHeadRecoveryNet

    def save(self, path: Path) -> None:
        torch.save(self.model.state_dict(), path)

    @classmethod
    def load(cls, path: Path, input_dim: int) -> "UnifiedModelBundle":
        model = MultiHeadRecoveryNet(input_dim=input_dim)
        model.load_state_dict(torch.load(path, map_location="cpu"))
        model.eval()
        return cls(model=model)

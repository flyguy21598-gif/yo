from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MODEL_DIR = ROOT / "artifacts"
MODEL_DIR.mkdir(exist_ok=True)


@dataclass(slots=True)
class AppConfig:
    raw_dir: Path = DATA_DIR / "raw"
    cleaned_dir: Path = DATA_DIR / "cleaned"
    labeled_dir: Path = DATA_DIR / "labeled"
    model_dir: Path = MODEL_DIR
    random_seed: int = int(os.getenv("RECOVERY_AI_SEED", "42"))
    max_features: int = int(os.getenv("RECOVERY_AI_MAX_FEATURES", "2048"))
    batch_size: int = int(os.getenv("RECOVERY_AI_BATCH_SIZE", "32"))
    epochs: int = int(os.getenv("RECOVERY_AI_EPOCHS", "3"))

    def ensure(self) -> "AppConfig":
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.cleaned_dir.mkdir(parents=True, exist_ok=True)
        self.labeled_dir.mkdir(parents=True, exist_ok=True)
        self.model_dir.mkdir(parents=True, exist_ok=True)
        return self


def get_config() -> AppConfig:
    return AppConfig().ensure()

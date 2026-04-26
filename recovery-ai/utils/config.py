from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MODEL_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"


@dataclass(slots=True)
class AppConfig:
    raw_dir: Path = DATA_DIR / "raw"
    cleaned_dir: Path = DATA_DIR / "cleaned"
    labeled_dir: Path = DATA_DIR / "labeled"
    dataset_dir: Path = DATA_DIR / "datasets"
    registry_file: Path = DATA_DIR / "raw" / "registry" / "sources.json"
    model_dir: Path = MODEL_DIR
    docs_dir: Path = DOCS_DIR
    random_seed: int = int(os.getenv("RECOVERY_AI_SEED", "42"))
    max_features: int = int(os.getenv("RECOVERY_AI_MAX_FEATURES", "2048"))
    batch_size: int = int(os.getenv("RECOVERY_AI_BATCH_SIZE", "32"))
    epochs: int = int(os.getenv("RECOVERY_AI_EPOCHS", "5"))

    def ensure(self) -> "AppConfig":
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.cleaned_dir.mkdir(parents=True, exist_ok=True)
        self.labeled_dir.mkdir(parents=True, exist_ok=True)
        self.dataset_dir.mkdir(parents=True, exist_ok=True)
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        self.model_dir.mkdir(parents=True, exist_ok=True)
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        return self


def get_config() -> AppConfig:
    return AppConfig().ensure()

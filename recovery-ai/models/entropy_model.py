from __future__ import annotations

from dataclasses import dataclass
import joblib
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer


@dataclass
class EntropyClassifier:
    pipeline: Pipeline | None = None

    def __post_init__(self) -> None:
        if self.pipeline is None:
            self.pipeline = Pipeline([
                ("tfidf", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), max_features=2048)),
                ("clf", LogisticRegression(max_iter=500)),
            ])

    def fit(self, texts: list[str], labels: list[int]) -> None:
        self.pipeline.fit(texts, labels)

    def predict_proba(self, texts: list[str]):
        return self.pipeline.predict_proba(texts)[:, 1]

    def save(self, path: Path) -> None:
        joblib.dump(self.pipeline, path)

    @classmethod
    def load(cls, path: Path) -> "EntropyClassifier":
        return cls(pipeline=joblib.load(path))

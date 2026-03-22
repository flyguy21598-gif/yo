from __future__ import annotations

import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer


def load_texts(jsonl_path: Path) -> list[str]:
    with jsonl_path.open("r", encoding="utf-8") as handle:
        return [json.loads(line)["text"] for line in handle]


class RecoveryTokenizer:
    def __init__(self, max_features: int = 2048) -> None:
        self.vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), max_features=max_features)

    def fit_transform(self, texts: list[str]):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts: list[str]):
        return self.vectorizer.transform(texts)

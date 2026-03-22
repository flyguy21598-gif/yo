from __future__ import annotations

import argparse
import re

from inference.ranking import combine_scores
from models.entropy_model import EntropyClassifier
from models.logic_model import LogicInferenceModel
from models.pattern_model import PatternDetector
from utils.config import get_config

WIF_PATTERN = re.compile(r"^[5KL][1-9A-HJ-NP-Za-km-z]{50,51}$")
SHA256_PATTERN = re.compile(r"^[a-fA-F0-9]{64}$")


def normalize_input(value: str) -> str:
    value = value.strip()
    if WIF_PATTERN.fullmatch(value):
        return f"wif {value}"
    if SHA256_PATTERN.fullmatch(value):
        return f"sha256 {value}"
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank recovery probability from WIF, SHA256, or free text input.")
    parser.add_argument("input_text")
    args = parser.parse_args()

    config = get_config()
    text = normalize_input(args.input_text)
    entropy = EntropyClassifier.load(config.model_dir / "entropy.joblib")
    pattern = PatternDetector.load(config.model_dir / "pattern.joblib")
    logic = LogicInferenceModel.load(config.model_dir / "logic.joblib")

    entropy_score = float(entropy.predict_proba([text])[0])
    pattern_score = float(pattern.predict_proba([text])[0])
    logic_score = float(logic.predict_proba([text])[0])
    unified_rank = combine_scores(entropy_score, pattern_score, logic_score)

    print({
        "input": args.input_text,
        "normalized": text,
        "entropy_score": round(entropy_score, 6),
        "pattern_score": round(pattern_score, 6),
        "logic_score": round(logic_score, 6),
        "recovery_probability": unified_rank,
    })


if __name__ == "__main__":
    main()

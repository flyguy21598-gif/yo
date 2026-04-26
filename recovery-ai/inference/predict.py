from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

from inference.ranking import combine_scores, confidence_band
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


def explain_scores(entropy_score: float, pattern_score: float, logic_score: float) -> list[str]:
    explanations: list[str] = []
    if entropy_score >= 0.6:
        explanations.append("High entropy-signal confidence from checksum/hash-like characteristics.")
    if pattern_score >= 0.6:
        explanations.append("Pattern detector found transcription/substitution-like structure.")
    if logic_score >= 0.6:
        explanations.append("Logic head identified coherent recovery reasoning clues.")
    if not explanations:
        explanations.append("Signals are weak or ambiguous; additional evidence is recommended.")
    return explanations


def model_fingerprint(config) -> str:
    payload = "|".join(
        str(path.name)
        for path in sorted(config.model_dir.glob("*.joblib"))
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def predict_one(value: str, entropy: EntropyClassifier, pattern: PatternDetector, logic: LogicInferenceModel, fingerprint: str) -> dict[str, object]:
    text = normalize_input(value)
    entropy_score = float(entropy.predict_proba([text])[0])
    pattern_score = float(pattern.predict_proba([text])[0])
    logic_score = float(logic.predict_proba([text])[0])
    recovery_probability = combine_scores(entropy_score, pattern_score, logic_score)

    return {
        "input": value,
        "normalized": text,
        "entropy_score": round(entropy_score, 6),
        "pattern_score": round(pattern_score, 6),
        "logic_score": round(logic_score, 6),
        "recovery_probability": recovery_probability,
        "confidence_band": confidence_band(recovery_probability),
        "explanations": explain_scores(entropy_score, pattern_score, logic_score),
        "model_fingerprint": fingerprint,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank recovery probability from WIF, SHA256, or free text input.")
    parser.add_argument("input_text", nargs="?", default=None)
    parser.add_argument("--input-file", default=None, help="Optional newline-delimited batch input file")
    parser.add_argument("--output", default=None, help="Optional output JSONL file for batch mode")
    args = parser.parse_args()

    config = get_config()
    entropy = EntropyClassifier.load(config.model_dir / "entropy.joblib")
    pattern = PatternDetector.load(config.model_dir / "pattern.joblib")
    logic = LogicInferenceModel.load(config.model_dir / "logic.joblib")
    fingerprint = model_fingerprint(config)

    if args.input_file:
        values = [line.strip() for line in Path(args.input_file).read_text(encoding="utf-8").splitlines() if line.strip()]
        rows = [predict_one(value, entropy, pattern, logic, fingerprint) for value in values]
        if args.output:
            with Path(args.output).open("w", encoding="utf-8") as handle:
                for row in rows:
                    handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        else:
            print(json.dumps(rows, ensure_ascii=False, indent=2))
        return

    if not args.input_text:
        raise ValueError("Either input_text or --input-file must be provided.")
    print(predict_one(args.input_text, entropy, pattern, logic, fingerprint))


if __name__ == "__main__":
    main()

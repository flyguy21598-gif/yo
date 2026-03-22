from __future__ import annotations

import json

from models.entropy_model import EntropyClassifier
from models.pattern_model import PatternDetector
from models.logic_model import LogicInferenceModel
from sparring.adversarial_generator import generate_variants
from utils.config import get_config


def disagreement_records(texts: list[str], entropy: EntropyClassifier, pattern: PatternDetector, logic: LogicInferenceModel):
    rows = []
    for text in texts:
        e = float(entropy.predict_proba([text])[0])
        p = float(pattern.predict_proba([text])[0])
        l = float(logic.predict_proba([text])[0])
        scores = {"entropy": e, "pattern": p, "logic": l}
        if max(scores.values()) - min(scores.values()) >= 0.35:
            rows.append({"text": text, "scores": scores, "labels": {k: int(v >= 0.5) for k, v in scores.items()}})
    return rows


def main() -> None:
    config = get_config()
    entropy = EntropyClassifier.load(config.model_dir / "entropy.joblib")
    pattern = PatternDetector.load(config.model_dir / "pattern.joblib")
    logic = LogicInferenceModel.load(config.model_dir / "logic.joblib")

    seeds = [
        "Possible WIF transcription issue with 0/O swap and checksum mismatch.",
        "Mnemonic phrase seems valid but wallet path logic is inconsistent.",
    ]
    expanded = [variant for seed in seeds for variant in generate_variants(seed)]
    rows = disagreement_records(expanded, entropy, pattern, logic)
    output = config.labeled_dir / "sparring_disagreements.jsonl"
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
    print(f"generated {len(rows)} disagreement rows at {output}")


if __name__ == "__main__":
    main()

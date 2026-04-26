from __future__ import annotations

import json
from pathlib import Path

from models.entropy_model import EntropyClassifier
from models.logic_model import LogicInferenceModel
from models.pattern_model import PatternDetector
from sparring.adversarial_generator import generate_variants
from utils.config import get_config


def disagreement_records(texts: list[str], entropy: EntropyClassifier, pattern: PatternDetector, logic: LogicInferenceModel):
    rows = []
    for text in texts:
        e = float(entropy.predict_proba([text])[0])
        p = float(pattern.predict_proba([text])[0])
        l = float(logic.predict_proba([text])[0])
        scores = {"entropy": e, "pattern": p, "logic": l}
        spread = max(scores.values()) - min(scores.values())
        if spread >= 0.35:
            rows.append(
                {
                    "text": text,
                    "scores": scores,
                    "spread": round(spread, 6),
                    "candidate_labels": {k: int(v >= 0.5) for k, v in scores.items()},
                    "triage_status": "pending_review",
                }
            )
    return rows


def append_feedback(dataset_path: Path, reviewed_rows: list[dict[str, object]]) -> int:
    accepted = [row for row in reviewed_rows if row.get("triage_status") == "accepted"]
    with dataset_path.open("a", encoding="utf-8") as handle:
        for row in accepted:
            row_out = {
                "text": row["text"],
                "labels": {
                    "entropy": {"value": int(row["candidate_labels"]["entropy"]), "confidence": 0.7, "provenance": {"sparring": 1}},
                    "pattern": {"value": int(row["candidate_labels"]["pattern"]), "confidence": 0.7, "provenance": {"sparring": 1}},
                    "logic": {"value": int(row["candidate_labels"]["logic"]), "confidence": 0.7, "provenance": {"sparring": 1}},
                },
            }
            handle.write(json.dumps(row_out, ensure_ascii=False) + "\n")
    return len(accepted)


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

    review_file = config.labeled_dir / "sparring_triage.jsonl"
    with review_file.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    retrain_ticket = {
        "generated_candidates": len(rows),
        "triage_file": str(review_file),
        "action": "mark rows accepted/rejected then run append-feedback workflow",
    }
    (config.labeled_dir / "retrain_ticket.json").write_text(json.dumps(retrain_ticket, indent=2), encoding="utf-8")
    print(f"generated {len(rows)} disagreement rows at {review_file}")


if __name__ == "__main__":
    main()

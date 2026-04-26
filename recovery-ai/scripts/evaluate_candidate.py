from __future__ import annotations

import json
from pathlib import Path


METRIC_FILES = [
    "entropy.metrics.json",
    "pattern.metrics.json",
    "logic.metrics.json",
]

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_metrics(model_dir: Path) -> dict[str, dict[str, object]]:
    metrics: dict[str, dict[str, object]] = {}
    for filename in METRIC_FILES:
        path = model_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"missing metric file: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        metrics[payload["model"]] = payload
    return metrics


def evaluate(metrics: dict[str, dict[str, object]]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for model_name, payload in metrics.items():
        train_rows = int(payload.get("train_rows", 0))
        if train_rows < 1:
            errors.append(f"{model_name}: train_rows must be > 0")
        positive_rate = float(payload.get("positive_rate", 0.0))
        if not 0.0 <= positive_rate <= 1.0:
            errors.append(f"{model_name}: positive_rate out of range")
    return (len(errors) == 0), errors


def main() -> None:
    model_dir = PROJECT_ROOT / "artifacts"
    output_dir = PROJECT_ROOT / "governance" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    metrics = load_metrics(model_dir)
    passed, errors = evaluate(metrics)

    summary = {
        "status": "pass" if passed else "fail",
        "errors": errors,
        "metrics": metrics,
    }

    json_out = output_dir / "candidate_evaluation.json"
    json_out.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    md_lines = [
        "# Candidate Evaluation",
        "",
        f"Status: **{summary['status']}**",
        "",
        "## Metrics",
    ]
    for name, payload in metrics.items():
        md_lines.append(f"- {name}: train_rows={payload['train_rows']}, positive_rate={payload['positive_rate']}")

    if errors:
        md_lines.extend(["", "## Errors", *[f"- {error}" for error in errors]])

    md_out = output_dir / "candidate_evaluation.md"
    md_out.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    if not passed:
        raise SystemExit(1)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

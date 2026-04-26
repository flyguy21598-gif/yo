from __future__ import annotations

import argparse
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
import tarfile


def file_hash(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            hasher.update(block)
    return hasher.hexdigest()


def collect_files(directory: Path, suffixes: tuple[str, ...]) -> list[Path]:
    if not directory.exists():
        return []
    files = [path for path in sorted(directory.rglob("*")) if path.is_file() and path.suffix in suffixes]
    return files


def build_audit_bundle(
    release_id: str,
    actor: str,
    reason: str,
    artifacts_dir: Path,
    incidents_log: Path,
    dr_drills_log: Path,
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    bundle_dir = output_dir / release_id
    bundle_dir.mkdir(parents=True, exist_ok=True)

    artifact_files = collect_files(artifacts_dir, (".joblib", ".pt", ".json"))
    entries = [{"path": str(path), "sha256": file_hash(path)} for path in artifact_files]

    manifest = {
        "release_id": release_id,
        "who": actor,
        "what": "model promotion/deployment",
        "when": datetime.now(tz=UTC).isoformat(),
        "why": reason,
        "artifacts": entries,
        "metrics_files": [entry for entry in entries if entry["path"].endswith(".metrics.json")],
        "incidents_log": str(incidents_log),
        "dr_drills_log": str(dr_drills_log),
    }

    manifest_path = bundle_dir / "audit_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    tar_path = output_dir / f"{release_id}.tar.gz"
    with tarfile.open(tar_path, "w:gz") as archive:
        archive.add(bundle_dir, arcname=release_id)

    digest_path = output_dir / f"{release_id}.sha256"
    digest_path.write_text(f"{file_hash(tar_path)}  {tar_path.name}\n", encoding="utf-8")
    return tar_path


def generate_compliance_report(audit_root: Path, incidents_log: Path, dr_drills_log: Path, output_file: Path) -> Path:
    bundles = sorted(audit_root.glob("*.tar.gz")) if audit_root.exists() else []
    incident_entries = incidents_log.read_text(encoding="utf-8").splitlines() if incidents_log.exists() else []
    drill_entries = dr_drills_log.read_text(encoding="utf-8").splitlines() if dr_drills_log.exists() else []

    lines = [
        "# Compliance Report",
        "",
        f"Generated: {datetime.now(tz=UTC).isoformat()}",
        "",
        "## Releases",
        f"- Total release bundles: {len(bundles)}",
    ]
    for bundle in bundles:
        lines.append(f"- {bundle.name}")

    lines.extend([
        "",
        "## Incidents",
        f"- Total incident records: {len(incident_entries)}",
    ])
    lines.extend([f"- {entry}" for entry in incident_entries[:50]])

    lines.extend([
        "",
        "## DR Drills",
        f"- Total DR drill records: {len(drill_entries)}",
    ])
    lines.extend([f"- {entry}" for entry in drill_entries[:50]])

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate immutable audit bundles and compliance reports.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    bundle_parser = subparsers.add_parser("bundle")
    bundle_parser.add_argument("--release-id", required=True)
    bundle_parser.add_argument("--actor", required=True)
    bundle_parser.add_argument("--reason", required=True)
    bundle_parser.add_argument("--artifacts-dir", default="recovery-ai/artifacts")
    bundle_parser.add_argument("--incidents-log", default="recovery-ai/governance/logs/incidents.jsonl")
    bundle_parser.add_argument("--dr-drills-log", default="recovery-ai/governance/logs/dr_drills.jsonl")
    bundle_parser.add_argument("--output-dir", default="recovery-ai/governance/releases")

    report_parser = subparsers.add_parser("compliance-report")
    report_parser.add_argument("--audit-root", default="recovery-ai/governance/releases")
    report_parser.add_argument("--incidents-log", default="recovery-ai/governance/logs/incidents.jsonl")
    report_parser.add_argument("--dr-drills-log", default="recovery-ai/governance/logs/dr_drills.jsonl")
    report_parser.add_argument("--output", default="recovery-ai/governance/reports/compliance_report.md")

    args = parser.parse_args()

    if args.command == "bundle":
        tar_path = build_audit_bundle(
            release_id=args.release_id,
            actor=args.actor,
            reason=args.reason,
            artifacts_dir=Path(args.artifacts_dir),
            incidents_log=Path(args.incidents_log),
            dr_drills_log=Path(args.dr_drills_log),
            output_dir=Path(args.output_dir),
        )
        print(f"created audit bundle: {tar_path}")
        return

    report_path = generate_compliance_report(
        audit_root=Path(args.audit_root),
        incidents_log=Path(args.incidents_log),
        dr_drills_log=Path(args.dr_drills_log),
        output_file=Path(args.output),
    )
    print(f"created compliance report: {report_path}")


if __name__ == "__main__":
    main()

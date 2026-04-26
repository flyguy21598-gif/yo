from __future__ import annotations

from pathlib import Path

from governance.validate_pr_metadata import parse_pr_fields, validate_fields
from governance.audit_bundle import generate_compliance_report


def test_parse_pr_fields() -> None:
    body = """
    Change-Type: deployment
    Promotion-Target: production
    Who: ops-team
    Why: release
    Artifacts: model-a
    Metrics: pass
    """
    fields = parse_pr_fields(body)
    assert fields["Change-Type"] == "deployment"
    assert fields["Promotion-Target"] == "production"


def test_validate_fields() -> None:
    fields = {
        "Change-Type": "deployment",
        "Promotion-Target": "staging",
        "Who": "ops",
        "Why": "deploy",
        "Artifacts": "x",
        "Metrics": "good",
    }
    policy = {
        "required_fields": ["Change-Type", "Promotion-Target", "Who", "Why", "Artifacts", "Metrics"],
        "allowed_change_types": ["deployment"],
        "allowed_promotion_targets": ["none", "staging", "production"],
    }
    assert validate_fields(fields, policy) == []


def test_compliance_report_generation(tmp_path: Path) -> None:
    audit_root = tmp_path / "releases"
    audit_root.mkdir(parents=True)
    (audit_root / "rel-1.tar.gz").write_text("x", encoding="utf-8")

    incidents = tmp_path / "incidents.jsonl"
    incidents.write_text('{"id":1,"status":"closed"}\n', encoding="utf-8")

    drills = tmp_path / "dr_drills.jsonl"
    drills.write_text('{"id":1,"result":"pass"}\n', encoding="utf-8")

    output = tmp_path / "report.md"
    report_path = generate_compliance_report(audit_root, incidents, drills, output)
    text = report_path.read_text(encoding="utf-8")
    assert "Total release bundles: 1" in text
    assert "Total incident records: 1" in text
    assert "Total DR drill records: 1" in text

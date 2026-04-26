# Governance and Compliance

This document defines production governance controls for model promotion and deployment.

## 1) Policy-as-code PR metadata checks

Pull requests that include model promotion or deployment changes must include these body fields:

- `Change-Type`
- `Promotion-Target`
- `Who`
- `Why`
- `Artifacts`
- `Metrics`

Validation is enforced by:

- `.github/workflows/governance-gates.yml`
- `recovery-ai/governance/validate_pr_metadata.py`
- `recovery-ai/governance/policies/pr_metadata_policy.json`

## 2) Two-person approval for production promotion

When `Promotion-Target: production`, governance gates require at least two approvals.

Enforcement is implemented in:

- `recovery-ai/governance/enforce_approval_policy.py`

## 3) Emergency override logging

If a PR includes `Emergency-Override-Reason`, the reason is logged as governance evidence and validated for minimum detail.

Governance logs are written to:

- `recovery-ai/governance/logs/approval_policy_checks.jsonl`
- `recovery-ai/governance/logs/pr_metadata_checks.jsonl`

## 4) Immutable audit bundles per release

Create release evidence bundles with:

- who / what / when / why
- artifact file hashes
- metrics file references
- incident and DR drill log pointers

Command:

```bash
PYTHONPATH=. python recovery-ai/governance/audit_bundle.py bundle \
  --release-id rel-2026-04-26 \
  --actor your-name \
  --reason "Promote validated model to production"
```

Output:

- `recovery-ai/governance/releases/<release-id>.tar.gz`
- `recovery-ai/governance/releases/<release-id>.sha256`

## 5) Periodic compliance report generation

Generate a summary report of releases, incidents, and DR drills:

```bash
PYTHONPATH=. python recovery-ai/governance/audit_bundle.py compliance-report
```

Output:

- `recovery-ai/governance/reports/compliance_report.md`

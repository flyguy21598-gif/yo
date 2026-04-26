# Recovery AI Scope and Threat Model

This project is scoped to **defensive recovery analysis** of user-provided artifacts (WIF, SHA256-like strings, and free text notes) for wallet backup restoration workflows.

## In Scope
- Ranking recovery probability for supplied text artifacts.
- Detecting entropy/pattern/logic signals in corpus text.
- Building reproducible offline datasets and models.

## Out of Scope
- Unauthorized wallet access attempts.
- Automated exploitation workflows.
- Remote data exfiltration.

## Safety Controls
- Local-only execution.
- No API keys.
- Source provenance and trust scores are tracked.
- Training data generated from disagreements is staged in triage before inclusion.

## Recovery Probability Definition
`recovery_probability` is a calibrated confidence score (0.0 to 1.0) estimating whether input evidence is likely useful for a legitimate recovery workflow.

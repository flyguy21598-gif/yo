# yo

## Codex Task Pipeline

This repository now contains a machine-readable **Codex Task Pipeline** for the requested trading-bot roadmap.

### Files

- `pipeline/codex-task-pipeline.json` — canonical phase, task, dependency, and agent definition.
- `docs/codex-task-pipeline.md` — human-readable guide for executing the roadmap with Codex.

### Quick start

1. Open `pipeline/codex-task-pipeline.json`.
2. Choose a release track (`paper_trading`, `live_trading_minimum`, or `full_platform`).
3. Start with the next unblocked task.
4. Use the task ID and acceptance criteria as the implementation prompt for Codex.

### First recommended tasks

- `P1-T1` Refactor trading bot into modular services
- `P1-T2` Implement centralized config system
- `P1-T3` Add structured logging
- `P1-T6` Implement environment validation script
- `P4-T19` Build global risk manager
- `P4-T20` Implement kill-switch

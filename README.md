# yo

## Codex Task Pipeline

This repository now includes a working **Codex Task Pipeline** utility for the trading-bot roadmap.

### What's included

- `pipeline/codex-task-pipeline.json` — canonical five-phase roadmap with tasks, dependencies, release tracks, and automation metadata.
- `pipeline/pipeline-state.json` — persisted task completion state.
- `src/codex_pipeline/` — loader, planner, validator, and CLI implementation.
- `tests/test_pipeline.py` — regression tests for validation, dependency enforcement, and state handling.

### Quick start

```bash
PYTHONPATH=src python -m codex_pipeline.cli validate
PYTHONPATH=src python -m codex_pipeline.cli summary
PYTHONPATH=src python -m codex_pipeline.cli next
```

### Example workflow

1. Validate the pipeline.
2. Ask for the next unblocked task.
3. Implement that task in the trading-bot codebase.
4. Mark it complete in `pipeline/pipeline-state.json`.
5. Re-check summary and release-track status.

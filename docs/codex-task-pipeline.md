# Codex Task Pipeline

The previous change only documented the roadmap. This version adds a **working pipeline utility** that can validate the roadmap, report phase progress, show the next unblocked tasks, and persist completion state.

## What is now implemented

- A **five-phase** canonical roadmap in `pipeline/codex-task-pipeline.json`.
- A persistent state file in `pipeline/pipeline-state.json`.
- A Python package in `src/codex_pipeline/` that can:
  - load pipeline definitions,
  - validate dependencies and release tracks,
  - report progress by phase,
  - identify the next executable tasks,
  - mark tasks complete while enforcing dependency order.
- Automated tests in `tests/test_pipeline.py`.

## Commands

All commands use the standard library only.

### Validate the pipeline

```bash
PYTHONPATH=src python -m codex_pipeline.cli validate
```

### Show phase progress

```bash
PYTHONPATH=src python -m codex_pipeline.cli summary
```

### Show the next unblocked tasks

```bash
PYTHONPATH=src python -m codex_pipeline.cli next
```

### Mark a task complete

```bash
PYTHONPATH=src python -m codex_pipeline.cli complete P1-T1
```

### Inspect a release track

```bash
PYTHONPATH=src python -m codex_pipeline.cli track paper_trading
```

## Why this addresses the previous gap

The repository now contains executable tooling rather than a documentation-only roadmap. Codex can use the pipeline utility to drive work phase by phase:

1. Validate the roadmap structure.
2. Ask for the next unblocked task.
3. Implement that task.
4. Mark it complete.
5. Re-run summary and release-track checks.

## Five implemented phases

1. `phase-1-core-engine`
2. `phase-2-strategy-intelligence`
3. `phase-3-ai-learning-layer`
4. `phase-4-money-control`
5. `phase-5-dashboard-control`

The earlier agent-system idea is preserved as a future extension in the pipeline metadata, but the pipeline itself now focuses on the requested five phases.

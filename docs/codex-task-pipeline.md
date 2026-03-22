# Codex Task Pipeline

This repository now treats the requested trading-bot roadmap as a **Codex Task Pipeline** instead of a flat feature wishlist.

## What changed

- The roadmap is encoded in `pipeline/codex-task-pipeline.json` as a machine-readable task graph.
- Every task has:
  - a stable task ID,
  - an owning agent,
  - explicit dependencies,
  - deliverables,
  - acceptance criteria.
- Release gates are called out so platform stability and money controls land before higher-risk AI features.

## Pipeline design principles

1. **Stability first**
   - Core engine work comes before strategy expansion.
   - Money-control tasks are promoted ahead of strategy and AI rollout.
2. **Agent ownership**
   - Strategy, risk, execution, and supervisor responsibilities are separated.
3. **Codex-friendly execution**
   - Tasks are small enough to become individual implementation prompts.
   - Dependencies make it clear what can be parallelized and what must wait.
4. **Safe rollout**
   - Paper-trading, live-minimum, and full-platform release tracks are defined separately.

## Recommended execution order

1. `phase-1-core-engine`
2. `phase-4-money-control`
3. `phase-2-strategy-intelligence`
4. `phase-3-ai-learning-layer`
5. `phase-5-dashboard-control`
6. `phase-6-agent-system`

This ordering intentionally moves **Money Control** ahead of later strategy and AI work because it is release-blocking for any live deployment.

## How to use with Codex

### 1. Pick a release track

- `paper_trading` for a safe initial milestone.
- `live_trading_minimum` for the first production-capable target.
- `full_platform` for the complete roadmap.

### 2. Select the next unblocked task

Use the dependency list in `pipeline/codex-task-pipeline.json` to identify the next task whose prerequisites are complete.

Example:

- `P1-T1` can start immediately.
- `P1-T2` must wait for `P1-T1`.
- `P1-T3` must wait for both `P1-T1` and `P1-T2`.

### 3. Turn one task into one Codex work item

Use a prompt template like this:

```text
Implement task P1-T4 from pipeline/codex-task-pipeline.json.

Task title: Build retry and failover execution wrapper.
Owner: execution-agent.
Deliverables:
- Kraken retry policy
- idempotent order wrapper
- failover path

Acceptance criteria:
- transient API failures are retried with backoff
- duplicate order placement is prevented
- failover outcome is logged and alertable

Constraints:
- preserve existing public interfaces where possible
- add tests for happy path and retry/failure path
- document config needed for retries and failover
```

### 4. Gate merges by acceptance criteria

A task should only be considered complete when:

- implementation is merged,
- tests pass,
- observability hooks are present,
- rollback or shutdown behavior is documented where relevant.

## Why this is a better structure

The original roadmap mixes foundational engineering, strategy research, AI experimentation, and operator tooling in one list. The task pipeline separates them into an execution system that Codex can work through reliably:

- **phases** define outcome-based milestones,
- **tasks** define concrete implementation units,
- **dependencies** prevent unsafe sequencing,
- **agent ownership** clarifies responsibility,
- **release tracks** support staged delivery.

## Suggested next milestone

If you want to start implementation immediately, the most defensible first milestone is:

- `P1-T1` modular services,
- `P1-T2` centralized config,
- `P1-T3` structured logging,
- `P1-T6` environment validation,
- `P4-T19` global risk manager,
- `P4-T20` kill-switch.

That creates a foundation strong enough to support paper trading and later strategy expansion.

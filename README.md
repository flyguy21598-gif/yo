# Temporal Graph Evolution Engine

Temporal Graph Evolution Engine is a production-ready Python 3.11+ simulation system for exploring branching graph timelines. It forks a shared graph state into temporal branches, evolves each branch independently, and reconciles the results into a unified federation state.

## Features

- **Temporal branches** with lifecycle management, divergence tracking, and seeded evolution.
- **Temporal manager** that forks, ticks, and cleans up expired branches.
- **Temporal convergence** that merges graph branches with weighted probabilistic edge selection.
- **Federation state** that consolidates graph state and shared branch memory.
- **Memory subsystem** supporting both text and vector memories.
- **Deterministic simulation mode** through seeded randomness.
- **Structured logging** using the standard `logging` module.
- **Production dependency model** using first-party `networkx` and `numpy` directly.

## Project structure

```text
.
├── main.py
├── requirements.txt
├── temporal_engine
│   ├── core
│   │   ├── federation.py
│   │   ├── memory.py
│   │   ├── temporal_branch.py
│   │   ├── temporal_convergence.py
│   │   └── temporal_manager.py
│   ├── simulation
│   │   └── runner.py
│   └── tests
│       ├── test_branch.py
│       ├── test_convergence.py
│       └── test_manager.py
└── README.md
```

## Requirements

- Python 3.11+
- `networkx`
- `numpy`
- `pytest`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the simulation

```bash
python main.py
```

The example entrypoint builds an initial cycle graph, runs five temporal evolution rounds, and logs the resulting global graph and merged memory state.

## Running tests

```bash
pytest temporal_engine/tests
```

## Architecture overview

### `TemporalBranch`

Each branch owns a forked graph plus associated memory. During `evolve()`, the branch performs one random perturbation from a small set:

- add a node and connect it into the graph,
- add an edge,
- remove an edge, or
- append new memory artifacts.

The branch also increases its `divergence_factor`, ages by one tick, and may transition from alive to dead based on its age and divergence.

### `TemporalManager`

The manager tracks active branches in a dictionary keyed by `branch_id`. It exposes:

- `fork()` to create new branches from the global federation state,
- `tick()` to evolve every active branch once, and
- `cleanup_dead_branches()` to remove dead branches efficiently.

### `TemporalConvergence`

Convergence merges all active branches using weighted logic:

- branch weight decreases as divergence grows,
- branch weight increases modestly with age,
- every candidate edge receives a weighted score based on the branches containing it, and
- the final edge set is sampled probabilistically from those scores.

The reconciler then updates federation graph state and merges all branch memories.

### `Federation`

Federation owns the authoritative global graph and global memory. It provides:

- `merge_memories()` to combine branch memories into one state, and
- `consolidate()` to publish the newest reconciled graph and memory.

## Notes on performance

- Branches fork with a single graph copy at creation time so evolution remains independent.
- Reconciliation uses union-of-edges scoring instead of expensive pairwise graph comparisons.
- Memory vectors are copied only when cloning or consolidating state.


## Benchmarking

Run reproducible runtime benchmarks for the full temporal evolution loop:

```bash
python -m temporal_engine.benchmark
```

This writes `benchmark_results.json` containing wall-clock timing and resulting global graph/memory cardinalities, making it simple to track regressions over time in CI or local runs.


## API reference

### `temporal_engine.core.temporal_branch.TemporalBranch`
- `evolve()`: advances one step with a randomized graph or memory perturbation.
- `terminate()`: marks the branch dead explicitly.
- Tracked attributes: `divergence_factor`, `age`, `creation_time`, `alive`.

### `temporal_engine.core.temporal_manager.TemporalManager`
- `fork(source_graph, source_memory)`: clones federation state into a new active branch.
- `tick()`: evolves all active branches by one step and clears dead branches.
- `cleanup_dead_branches()`: removes dead branches from active tracking.

### `temporal_engine.core.temporal_convergence.TemporalConvergence`
- `reconcile(federation, branches)`: weighted probabilistic edge merge plus federation consolidation.
- Weights combine inverse divergence with age bias for convergence voting.

### `temporal_engine.core.federation.Federation`
- `merge_memories(memories)`: combines branch memory states into one federated memory.
- `consolidate(graph, memory)`: atomically publishes the global graph/memory state.

### `temporal_engine.simulation.runner.temporal_evolution_round`
- Runs the simulation lifecycle (`fork -> evolve -> reconcile`) for configurable rounds.
- Supports deterministic seeded execution for reproducible experiments and tests.


## Quality gates

Use these commands for full verification in CI/local environments:

```bash
pytest temporal_engine/tests
pytest --cov=temporal_engine --cov-report=term-missing temporal_engine/tests
python main.py
python -m temporal_engine.benchmark
```

Benchmark output is persisted to `benchmark_results.json` and can be archived as a CI artifact for regression tracking.

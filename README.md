# Temporal Graph Evolution Engine

Temporal Graph Evolution Engine is a production-ready Python 3.11+ simulation system for exploring branching graph timelines. It forks a shared graph state into temporal branches, evolves each branch independently, and reconciles the results into a unified federation state.

## Features

- **Temporal branches** with lifecycle management, divergence tracking, and seeded evolution.
- **Temporal manager** that forks, ticks, and cleans up expired branches.
- **Temporal convergence** that merges graph branches with weighted probabilistic edge selection.
- **Federation state** that consolidates graph state and shared branch memory.
- **Memory subsystem** supporting both text and vector memories.
- **Deterministic testing mode** through seeded randomness.
- **Structured logging** using the standard `logging` module.
- **Offline-compatible dependency shims** that keep the demo runnable when `numpy` or `networkx` are unavailable in the execution environment, while still targeting the real libraries in `requirements.txt`.

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

If you are running in a restricted environment without package installation access, the project includes small compatibility shims used only as a fallback so the example and tests can still execute.

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

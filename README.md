# Revenant AI Bootstrap

A concrete MVP starter for an **Autonomous Offer Engine** that can produce launch plans for growth teams.

## What is included now

- Domain model for offers, audience segments, and experiments.
- Deterministic planning engine to allocate budget by channel and estimate pipeline.
- FastAPI app exposing `/health` and `/launch-plan`.
- CLI entrypoint for fast local usage.
- Unit tests for planning behavior.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

Run API:

```bash
uvicorn revenant.api.app:app --reload
```

Run CLI:

```bash
python -m revenant.cli --company "Acme" --budget 10000
```

## Optional large scaffold

If you still need a very large codebase skeleton for org/process bootstrapping:

```bash
python3 tools/generate_monorepo.py
```

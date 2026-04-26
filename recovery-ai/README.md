# Recovery AI

Recovery AI is a fully local framework for entropy/key recovery analysis research.

## Completed 10-Step Implementation

1. Scope and threat model documented in `docs/THREAT_MODEL.md`.
2. Source registry implemented at `data/raw/registry/sources.json` and loaded by `scraper/sources.py`.
3. Ingestion pipeline with dedupe/provenance implemented in `scraper/scrape.py` and `scraper/archive_scrape.py`.
4. Cleaner upgraded to rule+score filtering in `processing/cleaner.py`.
5. Weak-supervision labeler with confidence/provenance in `processing/labeler.py`.
6. Dataset versioning and split manifests in `processing/dataset_builder.py`.
7. Training scripts consume dataset snapshots and emit metrics JSON in `training/`.
8. Unified training upgraded with minibatch DataLoader in `training/train_unified.py`.
9. Sparring loop now creates triage queue and retrain ticket in `sparring/sparring_loop.py`.
10. Inference adds batch mode, confidence bands, explanations, and model fingerprint in `inference/predict.py`.

## Pipeline

```bash
cd recovery-ai
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. python scraper/scrape.py
PYTHONPATH=. python processing/cleaner.py recovery-ai/data/raw/scraped.jsonl --output recovery-ai/data/cleaned/cleaned.jsonl
PYTHONPATH=. python processing/labeler.py recovery-ai/data/cleaned/cleaned.jsonl --output recovery-ai/data/labeled/labeled.jsonl
PYTHONPATH=. python processing/dataset_builder.py recovery-ai/data/labeled/labeled.jsonl --output-dir recovery-ai/data/datasets
PYTHONPATH=. python training/train_entropy.py
PYTHONPATH=. python training/train_pattern.py
PYTHONPATH=. python training/train_logic.py
PYTHONPATH=. python training/train_unified.py
PYTHONPATH=. python sparring/sparring_loop.py
PYTHONPATH=. python inference/predict.py "Possible WIF checksum mismatch"
```

## Batch Inference

```bash
PYTHONPATH=. python inference/predict.py --input-file inputs.txt --output predictions.jsonl
```

## Local Tests

```bash
PYTHONPATH=. python -m pytest tests -q
```


## Governance

- Governance gates and compliance workflows are documented in `docs/GOVERNANCE_AND_COMPLIANCE.md`.
- PR metadata, two-person approval enforcement, immutable audit bundles, and compliance reports are implemented under `governance/`.


## GitHub Automation

- `.github/workflows/ci.yml` runs compile, tests, and a pipeline smoke test on PRs/pushes.
- `.github/workflows/train-and-evaluate.yml` performs scheduled/on-demand candidate training, evaluation, and immutable audit bundle creation.
- `.github/workflows/governance-gates.yml` enforces PR metadata policy and production approval gates.

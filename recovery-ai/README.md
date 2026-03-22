# Recovery AI

Recovery AI is a fully local scaffold for an offline entropy and key-recovery research workflow. Step 1 establishes the repository structure, runnable modules, and a Python 3.11-compatible dependency set.

## What is included

- `scraper/`: local and HTTP scraping entry points.
- `processing/`: cleaning, filtering, labeling, and tokenization utilities.
- `models/`: three standalone classifiers plus a PyTorch multi-head model.
- `training/`: separate training scripts for each model and the unified model.
- `sparring/`: disagreement-driven data generation loop.
- `inference/`: local probability ranking from WIF, SHA256, or free text.
- `data/`: raw, cleaned, and labeled JSONL stores.
- `notebook/`: bootstrap notebook for pipeline walkthrough.

## Quick start

```bash
cd recovery-ai
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. python scraper/scrape.py
PYTHONPATH=. python processing/cleaner.py
PYTHONPATH=. python processing/labeler.py
PYTHONPATH=. python training/train_entropy.py
PYTHONPATH=. python training/train_pattern.py
PYTHONPATH=. python training/train_logic.py
PYTHONPATH=. python inference/predict.py "Possible WIF checksum mismatch after manual transcription"
```

## Pipeline order

1. Scrape or ingest local sources.
2. Clean and filter recovery-relevant text.
3. Apply heuristic labels for entropy, pattern, and logic signals.
4. Train independent models.
5. Run inference and sparring loops locally.

## Notes

- All code paths run locally and do not require API keys.
- The default seed corpus is written into `data/raw/local_seed.txt` during the first scrape run.
- The unified model stores weights in `artifacts/unified.pt`.

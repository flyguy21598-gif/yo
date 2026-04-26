#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

printf "\n✅ Codespace bootstrap completed.\n"
printf "Run tests with: pytest temporal_engine/tests\n"

"""PowerKit CLI: data ops toolkit with parsing, profiling, anomaly scoring, and rules."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
from .engine import analyze_csv, summarize_jsonl


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="powerkit", description="Powerful data operations toolkit")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("analyze-csv", help="Profile CSV and compute anomaly scores")
    a.add_argument("path")
    a.add_argument("--max-rows", type=int, default=50000)

    j = sub.add_parser("summarize-jsonl", help="Summarize JSONL events")
    j.add_argument("path")

    args = p.parse_args(argv)
    if args.cmd == "analyze-csv":
        result = analyze_csv(Path(args.path), args.max_rows)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    if args.cmd == "summarize-jsonl":
        result = summarize_jsonl(Path(args.path))
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

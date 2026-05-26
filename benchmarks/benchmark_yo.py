import argparse
import json
import pathlib
import shutil
import statistics
import subprocess
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yo


def benchmark(label: str, fn, runs: int) -> dict[str, float]:
    timings = []
    for _ in range(runs):
        start = time.perf_counter()
        fn()
        timings.append(time.perf_counter() - start)
    return {
        "runs": runs,
        "mean_ms": statistics.mean(timings) * 1000,
        "p95_ms": statistics.quantiles(timings, n=20)[-1] * 1000,
    }


def run_hot_benchmarks(runs: int) -> dict[str, dict[str, float]]:
    blueprint = yo.build_blueprint("focus", seed="alpha")
    return {
        "build_one": benchmark("build_one", lambda: yo.build_blueprint("focus", seed="alpha"), runs),
        "build_three": benchmark(
            "build_three",
            lambda: yo.build_blueprints("focus", seed="alpha", count=3, profile="general"),
            runs,
        ),
        "render_markdown": benchmark("render_markdown", lambda: yo.render_markdown(blueprint), runs),
        "render_json": benchmark("render_json", lambda: yo.render_json(blueprint), runs),
    }


def clear_pycache() -> None:
    for path in ROOT.rglob("__pycache__"):
        shutil.rmtree(path, ignore_errors=True)


def run_cold_process(command: list[str], cwd: pathlib.Path) -> float:
    start = time.perf_counter()
    subprocess.run(command, cwd=cwd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return time.perf_counter() - start


def run_cold_benchmarks(runs: int) -> dict[str, dict[str, float]]:
    timings = []
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = pathlib.Path(tmpdir) / "out.json"
        for _ in range(runs):
            clear_pycache()
            duration = run_cold_process(
                [
                    "python",
                    "yo.py",
                    "focus",
                    "--json",
                    "--count",
                    "3",
                    "--profile",
                    "product",
                    "--output",
                    str(out_path),
                ],
                cwd=ROOT,
            )
            timings.append(duration)
    return {
        "cold_cli_json_count3": {
            "runs": runs,
            "mean_ms": statistics.mean(timings) * 1000,
            "p95_ms": statistics.quantiles(timings, n=20)[-1] * 1000,
        }
    }


def print_results(results: dict[str, dict[str, float]]) -> None:
    for label, values in results.items():
        print(f"[{label}] runs={int(values['runs'])}")
        print(f"[{label}] mean_ms={values['mean_ms']:.3f}")
        print(f"[{label}] p95_ms={values['p95_ms']:.3f}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run hot/cold benchmarks for yo")
    parser.add_argument("--runs", type=int, default=200, help="Number of runs per benchmark group")
    parser.add_argument(
        "--mode",
        choices=["hot", "cold", "all"],
        default="all",
        help="Benchmark mode",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.runs < 20:
        raise SystemExit("runs must be at least 20 for stable p95 output")

    output: dict[str, dict[str, float]] = {}
    if args.mode in {"hot", "all"}:
        output.update(run_hot_benchmarks(args.runs))
    if args.mode in {"cold", "all"}:
        output.update(run_cold_benchmarks(args.runs))

    if args.json:
        print(json.dumps(output, indent=2))
    else:
        print_results(output)


if __name__ == "__main__":
    main()

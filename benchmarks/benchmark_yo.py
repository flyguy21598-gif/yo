import pathlib
import statistics
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yo


def benchmark(label: str, fn, runs: int = 500) -> None:
    timings = []
    for _ in range(runs):
        start = time.perf_counter()
        fn()
        timings.append(time.perf_counter() - start)
    print(f"[{label}] runs={runs}")
    print(f"[{label}] mean_ms={statistics.mean(timings) * 1000:.3f}")
    print(f"[{label}] p95_ms={statistics.quantiles(timings, n=20)[-1] * 1000:.3f}")


def main() -> None:
    benchmark("build_one", lambda: yo.build_blueprint("focus", seed="alpha"))
    benchmark("build_three", lambda: yo.build_blueprints("focus", seed="alpha", count=3))

    blueprint = yo.build_blueprint("focus", seed="alpha")
    benchmark("render_markdown", lambda: yo.render_markdown(blueprint))
    benchmark("render_json", lambda: yo.render_json(blueprint))


if __name__ == "__main__":
    main()

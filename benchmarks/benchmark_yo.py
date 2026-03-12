import pathlib
import statistics
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import yo


def main() -> None:
    timings = []
    for _ in range(200):
        start = time.perf_counter()
        yo.build_blueprint("focus", seed="alpha")
        timings.append(time.perf_counter() - start)
    print("runs=200")
    print(f"mean_ms={statistics.mean(timings) * 1000:.3f}")
    print(f"p95_ms={statistics.quantiles(timings, n=20)[-1] * 1000:.3f}")


if __name__ == "__main__":
    main()

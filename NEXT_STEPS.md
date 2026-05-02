# Next 10 Steps for the Code and Repository

1. **Add baseline reproducibility support** by introducing a `--seed` CLI option and emitting the seed in run logs/results.
2. **Refactor core modules** by splitting `qga.py` into focused files (for example `simulator.py`, `genome.py`, `evolution.py`, `cli.py`) to improve maintainability.
3. **Add automated tests** for gate application, GHZ fidelity calculation, mutation/crossover validity, and elitism behavior.
4. **Add CI checks** (format, lint, and tests) using GitHub Actions to protect `main` from regressions.
5. **Introduce structured run outputs** (JSON/CSV) for best fitness per generation and final circuit metadata to support experiment tracking.
6. **Implement simple experiment presets** (small/medium/large) so users can run benchmarked configurations with a single flag.
7. **Improve observability** by printing concise per-generation telemetry (best/mean fitness, diversity proxy, mutation rate).
8. **Document algorithm internals** in a dedicated `docs/` page with architecture diagrams and operator definitions.
9. **Add lightweight profiling hooks** (timing for evaluation/selection/mutation) to identify and optimize bottlenecks.
10. **Create a contribution guide** (`CONTRIBUTING.md`) covering coding standards, test expectations, and how to propose new operators.

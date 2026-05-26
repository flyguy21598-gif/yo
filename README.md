# yo

Yo is a zero-dependency command-line generator that turns a theme into a powerful, unique blueprint. It is designed for rapid planning, deterministic reproducibility, and realistic MVP workflow iteration.

## Usage

Generate one blueprint in Markdown:

```bash
python yo.py "strategic clarity"
```

Generate JSON output:

```bash
python yo.py "strategic clarity" --json
```

Use a seed for deterministic variation:

```bash
python yo.py "strategic clarity" --seed "alpha"
```

Generate multiple alternatives for review:

```bash
python yo.py "strategic clarity" --count 3
```

Tailor protocol language to your workflow (`general`, `founder`, `product`, `creator`):

```bash
python yo.py "strategic clarity" --profile founder
```

Write output to a file (directories auto-create):

```bash
python yo.py "strategic clarity" --count 3 --output plans/blueprints.md
```

## Output Sections

Each blueprint includes:

- Title and tagline
- Power Core
- Unique Edge
- Protocol
- Signature Metrics
- Leverage Stack
- Threats to Disarm
- Invocation

## Testing

```bash
python -m unittest discover -s tests
```

## Benchmarking

Hot benchmarks (in-process build/render):

```bash
python benchmarks/benchmark_yo.py --mode hot --runs 200
```

Cold-space benchmark (fresh CLI process with `__pycache__` cleared before each run):

```bash
python benchmarks/benchmark_yo.py --mode cold --runs 200
```

All benchmarks together:

```bash
python benchmarks/benchmark_yo.py --mode all --runs 200
```

Machine-readable benchmark report:

```bash
python benchmarks/benchmark_yo.py --mode all --runs 200 --json
```

Example output (machine-dependent):

```text
[build_one] runs=200
[build_one] mean_ms=0.036
[build_one] p95_ms=0.051
[build_three] runs=200
[build_three] mean_ms=0.105
[build_three] p95_ms=0.130
[render_markdown] runs=200
[render_markdown] mean_ms=0.024
[render_markdown] p95_ms=0.033
[render_json] runs=200
[render_json] mean_ms=0.073
[render_json] p95_ms=0.111
[cold_cli_json_count3] runs=200
[cold_cli_json_count3] mean_ms=79.500
[cold_cli_json_count3] p95_ms=91.300
```

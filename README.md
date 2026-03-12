# yo

Yo is a zero-dependency command-line generator that turns a theme into a powerful, unique blueprint. It is designed for rapid planning, deterministic reproducibility, and MVP-level practical usage.

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

Generate multiple alternatives (great for team selection):

```bash
python yo.py "strategic clarity" --count 3
```

Write output to a file (directories are auto-created):

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

```bash
python benchmarks/benchmark_yo.py
```

Example benchmark output (machine-dependent):

```text
[build_one] runs=500
[build_one] mean_ms=0.095
[build_one] p95_ms=0.160
[build_three] runs=500
[build_three] mean_ms=0.251
[build_three] p95_ms=0.420
[render_markdown] runs=500
[render_markdown] mean_ms=0.014
[render_markdown] p95_ms=0.021
[render_json] runs=500
[render_json] mean_ms=0.023
[render_json] p95_ms=0.032
```

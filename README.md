# Quantum Genetic Algorithm (QGA) for GHZ-State Synthesis

This repository contains a **dependency-free** implementation of a Quantum Genetic Algorithm (QGA) that evolves quantum circuits toward an \(n\)-qubit GHZ state.

It is designed to run in restricted environments where package installation may be blocked.

## What is implemented

- Gene-based circuit representation (`GateSpec`)
- Built-in statevector simulator (no Qiskit/NumPy dependency)
- Fidelity objective for GHZ-state preparation
- Tournament selection + elitism
- Two-point crossover
- Parameter and structural mutation (insert/delete/swap)
- Adaptive mutation/crossover schedules

## Objective function

For \(n\) qubits:

\[
|\mathrm{GHZ}_n\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle^{\otimes n} + |1\rangle^{\otimes n}\right)
\]

If a candidate circuit prepares \(|\psi\rangle\), fitness is:

\[
F = |\langle \mathrm{GHZ}_n | \psi \rangle|^2,
\]

with \(0 \leq F \leq 1\).

## Run

```bash
python qga.py
```

Optional tuning:

```bash
python qga.py --qubits 10 --population 48 --generations 20 --max-depth 14
```

## Notes on scalability

This project uses full statevector simulation, so memory/time scale exponentially with qubit count. Defaults are selected to be runnable in normal development environments.

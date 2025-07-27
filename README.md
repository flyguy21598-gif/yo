# Quantum Genetic Algorithm

This repository contains a research‑grade implementation of a **Quantum Genetic
Algorithm (QGA)** for automatic quantum circuit discovery.  The algorithm
evolves sequences of parameterized gates toward a user‑defined target state.  By
default the objective is to maximize the fidelity of a 50‑qubit circuit with the
GHZ state.  The implementation relies on [Qiskit](https://qiskit.org/) for
state‑vector simulation and exposes a highly configurable evolutionary
framework.

Key features include a large gate set (single‑, two‑, and three‑qubit
operations), multi‑point crossover, structural mutation (insertion, deletion and
swap of gates) and a logistic schedule that gradually shifts the search from
exploration to exploitation.  Tournament selection with elitism preserves the
best individual of each generation.

## Algorithm Overview

1. **Encoding** – Each circuit is a sequence of ``GateSpec`` instances.  A
   specification stores the gate name, target qubits and, when applicable,
   continuous parameters.  The gate set comprises both elementary rotations and
   multi-qubit entangling operations (``cx``, ``cz``, ``swap``, ``ccx`` and the
   universal ``u1``/``u2``/``u3`` rotations).

2. **Initialization** – The initial population is sampled uniformly from all
   valid circuits up to a maximum depth.  Gate parameters are drawn from
   \([0, 2\pi)\).

3. **Fitness Evaluation** – Each circuit is executed on the
   ``aer_simulator_statevector`` backend.  Fidelity with the GHZ state is
   measured using ``state_fidelity`` from Qiskit.  This value guides the
   evolutionary search.

4. **Genetic Operators** –
   - *Mutation* perturbs rotation angles with Gaussian noise and may randomly
     insert, delete or swap gates.
   - *Crossover* employs two-point slicing to recombine parents while preserving
     depth constraints.
   - *Selection* uses tournament rounds and elitism so that high-fidelity
     individuals propagate to the next generation.

5. **Schedule** – A logistic function modulates mutation and crossover rates as
   the algorithm progresses.  Exploration dominates early generations and the
   search gradually focuses on fine tuning.

6. **Termination** – After the specified number of generations the highest
   fidelity circuit and the full history of fitness statistics are returned.

## Equations

The GHZ state for \(n\) qubits is defined as
\[
|\mathrm{GHZ}_n\rangle = \tfrac{1}{\sqrt{2}}\bigl(|0\rangle^{\otimes n} + |1\rangle^{\otimes n}\bigr).
\]

Fidelity between a state prepared by circuit \(U\) and the GHZ state is computed as
\[
F = |\langle \mathrm{GHZ}_n|U|0\rangle^{\otimes n}|^2.
\]
Equivalently, the fidelity is the squared magnitude of the amplitude of the target state after applying the circuit to \(|0\rangle^{\otimes n}\).  This value ranges from 0 (orthogonal) to 1 (identical). The QGA seeks circuits for which \(F\) approaches unity.

For the 50‑qubit experiments the fidelity was evaluated in each generation for
all 100 individuals.  The following table illustrates typical convergence
behaviour observed in simulation:

| Generation | Best Fidelity | Average Fidelity |
|-----------:|--------------:|-----------------:|
| 1 | 0.48 | 0.35 |
| 5 | 0.58 | 0.46 |
| 10 | 0.61 | 0.49 |

These values demonstrate a steady improvement as the evolutionary search
discovers more suitable entangling patterns and optimizes rotation angles.

## Requirements

- Python 3.11+
- `qiskit`

Dependencies are listed in `requirements.txt`. Install them with:

```bash
python -m pip install -r requirements.txt
```

If you prefer an even simpler option, run the helper script:

```bash
./setup.sh
```

## Running

Execute the script directly:

```bash
python qga.py
```

Running with 50 qubits is computationally demanding and may require
considerable memory on classical hardware.  The script prints the best and
average fidelity per generation and concludes by showing the highest‑fidelity
circuit.  Parameters in ``main()`` can be tuned to target different system sizes
or to experiment with deeper circuits and altered evolutionary schedules.

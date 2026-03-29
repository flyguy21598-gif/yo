"""Dependency-free Quantum Genetic Algorithm for GHZ-state synthesis.

This implementation avoids external packages so `python qga.py` runs in restricted
environments. It uses a small built-in statevector simulator and evolves gate
sequences toward an n-qubit GHZ state.
"""

from __future__ import annotations

import argparse
import cmath
import math
import random
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class GateSpec:
    """Compact circuit gene encoding."""

    name: str
    qubits: tuple[int, ...]
    params: tuple[float, ...] = ()


class StatevectorSimulator:
    """Minimal statevector simulator supporting the gates used by the QGA."""

    def __init__(self, num_qubits: int) -> None:
        self.n = num_qubits
        self.dim = 1 << num_qubits

    def zero_state(self) -> list[complex]:
        state = [0j] * self.dim
        state[0] = 1 + 0j
        return state

    def apply_single(self, state: list[complex], qubit: int, m: tuple[tuple[complex, complex], tuple[complex, complex]]) -> None:
        step = 1 << qubit
        period = step << 1
        for base in range(0, self.dim, period):
            for offset in range(step):
                i0 = base + offset
                i1 = i0 + step
                a0 = state[i0]
                a1 = state[i1]
                state[i0] = m[0][0] * a0 + m[0][1] * a1
                state[i1] = m[1][0] * a0 + m[1][1] * a1

    def apply_cx(self, state: list[complex], control: int, target: int) -> None:
        if control == target:
            return
        cbit = 1 << control
        tbit = 1 << target
        for i in range(self.dim):
            if i & cbit and not (i & tbit):
                j = i | tbit
                state[i], state[j] = state[j], state[i]

    def apply_cz(self, state: list[complex], control: int, target: int) -> None:
        if control == target:
            return
        cbit = 1 << control
        tbit = 1 << target
        for i in range(self.dim):
            if i & cbit and i & tbit:
                state[i] = -state[i]

    def apply_swap(self, state: list[complex], q0: int, q1: int) -> None:
        if q0 == q1:
            return
        b0 = 1 << q0
        b1 = 1 << q1
        for i in range(self.dim):
            bit0 = 1 if (i & b0) else 0
            bit1 = 1 if (i & b1) else 0
            if bit0 == 0 and bit1 == 1:
                j = i ^ (b0 | b1)
                state[i], state[j] = state[j], state[i]

    def run(self, num_qubits: int, circuit: Sequence[GateSpec]) -> list[complex]:
        if num_qubits != self.n:
            raise ValueError("Simulator qubit mismatch")

        state = self.zero_state()
        sqrt2 = math.sqrt(2)

        for gate in circuit:
            name = gate.name
            if name == "h":
                m = ((1 / sqrt2, 1 / sqrt2), (1 / sqrt2, -1 / sqrt2))
                self.apply_single(state, gate.qubits[0], m)
            elif name == "x":
                self.apply_single(state, gate.qubits[0], ((0, 1), (1, 0)))
            elif name == "z":
                self.apply_single(state, gate.qubits[0], ((1, 0), (0, -1)))
            elif name == "rx":
                theta = gate.params[0]
                c = math.cos(theta / 2)
                s = -1j * math.sin(theta / 2)
                self.apply_single(state, gate.qubits[0], ((c, s), (s, c)))
            elif name == "ry":
                theta = gate.params[0]
                c = math.cos(theta / 2)
                s = math.sin(theta / 2)
                self.apply_single(state, gate.qubits[0], ((c, -s), (s, c)))
            elif name == "rz":
                theta = gate.params[0]
                e0 = cmath.exp(-1j * theta / 2)
                e1 = cmath.exp(1j * theta / 2)
                self.apply_single(state, gate.qubits[0], ((e0, 0), (0, e1)))
            elif name == "cx":
                self.apply_cx(state, gate.qubits[0], gate.qubits[1])
            elif name == "cz":
                self.apply_cz(state, gate.qubits[0], gate.qubits[1])
            elif name == "swap":
                self.apply_swap(state, gate.qubits[0], gate.qubits[1])
            else:
                raise ValueError(f"Unsupported gate: {name}")

        return state


class QuantumGeneticAlgorithm:
    """Evolve circuits that maximize fidelity to an n-qubit GHZ state."""

    def __init__(
        self,
        num_qubits: int,
        population_size: int,
        generations: int,
        mutation_rate: float,
        crossover_rate: float,
        max_depth: int,
        tournament_k: int,
        seed: int | None = None,
    ) -> None:
        if num_qubits < 2:
            raise ValueError("num_qubits must be >= 2 for GHZ synthesis")

        self.rng = random.Random(seed)
        self.num_qubits = num_qubits
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.max_depth = max_depth
        self.tournament_k = max(2, min(tournament_k, population_size))

        self.gate_set = ("h", "x", "z", "rx", "ry", "rz", "cx", "cz", "swap")
        self.sim = StatevectorSimulator(num_qubits)
        self.ghz_norm = math.sqrt(2)
        self.ghz_idx = (0, (1 << num_qubits) - 1)

    def _random_gate(self) -> GateSpec:
        gate = self.rng.choice(self.gate_set)
        if gate in {"cx", "cz", "swap"}:
            q0, q1 = self.rng.sample(range(self.num_qubits), 2)
            return GateSpec(gate, (q0, q1))

        q = self.rng.randrange(self.num_qubits)
        if gate in {"rx", "ry", "rz"}:
            return GateSpec(gate, (q,), (self.rng.uniform(0.0, math.tau),))
        return GateSpec(gate, (q,))

    def _random_individual(self) -> list[GateSpec]:
        depth = self.rng.randint(1, self.max_depth)
        return [self._random_gate() for _ in range(depth)]

    def _initialize_population(self) -> list[list[GateSpec]]:
        return [self._random_individual() for _ in range(self.population_size)]

    def _evaluate_fitness(self, individual: Sequence[GateSpec]) -> float:
        sv = self.sim.run(self.num_qubits, individual)
        overlap = (sv[self.ghz_idx[0]] + sv[self.ghz_idx[1]]) / self.ghz_norm
        return float((overlap.conjugate() * overlap).real)

    def _mutate(self, individual: list[GateSpec]) -> list[GateSpec]:
        out: list[GateSpec] = []
        for gene in individual:
            if self.rng.random() < self.mutation_rate:
                if gene.params and self.rng.random() < 0.7:
                    jittered = tuple((p + self.rng.gauss(0.0, 0.12)) % math.tau for p in gene.params)
                    out.append(GateSpec(gene.name, gene.qubits, jittered))
                else:
                    out.append(self._random_gate())
            else:
                out.append(gene)

        if self.rng.random() < self.mutation_rate and len(out) < self.max_depth:
            out.insert(self.rng.randrange(len(out) + 1), self._random_gate())
        if self.rng.random() < self.mutation_rate and len(out) > 1:
            del out[self.rng.randrange(len(out))]
        if self.rng.random() < self.mutation_rate and len(out) > 1:
            i, j = self.rng.sample(range(len(out)), 2)
            out[i], out[j] = out[j], out[i]
        return out

    def _crossover(self, p1: list[GateSpec], p2: list[GateSpec]) -> list[GateSpec]:
        min_len = min(len(p1), len(p2))
        if min_len < 2:
            return p1[:]
        c1 = self.rng.randint(1, min_len - 1)
        c2 = self.rng.randint(c1, min_len)
        child = p1[:c1] + p2[c1:c2] + p1[c2:]
        return child[: self.max_depth]

    def _tournament_pick(self, population: list[list[GateSpec]], fitnesses: list[float]) -> list[GateSpec]:
        contender_ids = self.rng.sample(range(len(population)), self.tournament_k)
        winner_idx = max(contender_ids, key=lambda idx: fitnesses[idx])
        return population[winner_idx]

    def _adaptive_rates(self, generation_idx: int) -> None:
        progress = (generation_idx + 1) / self.generations
        self.mutation_rate = 0.45 / (1.0 + math.exp(6.0 * (progress - 0.5))) + 0.03
        self.crossover_rate = min(0.95, 0.55 + 0.4 * progress)

    def run(self) -> tuple[list[GateSpec], list[tuple[float, float]]]:
        population = self._initialize_population()
        history: list[tuple[float, float]] = []

        for gen in range(self.generations):
            fitnesses = [self._evaluate_fitness(ind) for ind in population]
            best = max(fitnesses)
            avg = sum(fitnesses) / len(fitnesses)
            history.append((best, avg))

            elite_idx = fitnesses.index(best)
            next_population: list[list[GateSpec]] = [population[elite_idx][:]]

            while len(next_population) < self.population_size:
                p1 = self._tournament_pick(population, fitnesses)
                p2 = self._tournament_pick(population, fitnesses)
                child = self._crossover(p1, p2) if self.rng.random() < self.crossover_rate else p1[:]
                next_population.append(self._mutate(child))

            population = next_population
            self._adaptive_rates(gen)

        final_scores = [self._evaluate_fitness(ind) for ind in population]
        best_idx = max(range(len(population)), key=lambda i: final_scores[i])
        return population[best_idx], history

    def pretty_print_circuit(self, individual: Sequence[GateSpec]) -> str:
        lines = []
        for i, g in enumerate(individual):
            params = "" if not g.params else "(" + ", ".join(f"{p:.4f}" for p in g.params) + ")"
            qtxt = ", ".join(str(q) for q in g.qubits)
            lines.append(f"{i:02d}: {g.name}{params} q[{qtxt}]")
        return "\n".join(lines) if lines else "<empty circuit>"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Dependency-free QGA for GHZ-state synthesis")
    parser.add_argument("--qubits", type=int, default=8, help="Number of qubits (default: 8)")
    parser.add_argument("--population", type=int, default=36, help="Population size (default: 36)")
    parser.add_argument("--generations", type=int, default=12, help="Generations (default: 12)")
    parser.add_argument("--mutation", type=float, default=0.25, help="Initial mutation rate (default: 0.25)")
    parser.add_argument("--crossover", type=float, default=0.75, help="Initial crossover rate (default: 0.75)")
    parser.add_argument("--max-depth", type=int, default=10, help="Maximum gate count (default: 10)")
    parser.add_argument("--tournament-k", type=int, default=3, help="Tournament size (default: 3)")
    parser.add_argument("--seed", type=int, default=7, help="Random seed (default: 7)")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    qga = QuantumGeneticAlgorithm(
        num_qubits=args.qubits,
        population_size=args.population,
        generations=args.generations,
        mutation_rate=args.mutation,
        crossover_rate=args.crossover,
        max_depth=args.max_depth,
        tournament_k=args.tournament_k,
        seed=args.seed,
    )

    best, history = qga.run()
    for i, (best_fit, avg_fit) in enumerate(history, start=1):
        print(f"Generation {i:02d} | best={best_fit:.6f} avg={avg_fit:.6f}")

    final_fidelity = qga._evaluate_fitness(best)
    print(f"Final best fidelity: {final_fidelity:.6f}")
    print("Best circuit:")
    print(qga.pretty_print_circuit(best))


if __name__ == "__main__":
    main()

"""Quantum Genetic Algorithm for state fidelity maximization.

This version integrates several advanced evolutionary strategies,
including tournament selection, multi-point crossover, and a logistic
schedule for mutation and crossover probabilities.  Circuits evolve
toward a high-fidelity GHZ state on an arbitrary number of qubits.
"""

import math
import random
from dataclasses import dataclass
from typing import List, Tuple

from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector, state_fidelity


@dataclass
class GateSpec:
    """Representation of a quantum gate with optional parameters."""

    name: str
    qubits: Tuple[int, ...]
    params: Tuple[float, ...] | None = None

    def apply(self, circuit: QuantumCircuit) -> None:
        if self.name in {"rx", "ry", "rz"} and self.params is not None:
            getattr(circuit, self.name)(self.params[0], *self.qubits)
        elif self.name in {"u1", "u2", "u3"} and self.params is not None:
            getattr(circuit, self.name)(*self.params, *self.qubits)
        elif self.name in {"cx", "cz", "swap", "ccx"}:
            getattr(circuit, self.name)(*self.qubits)
        else:
            getattr(circuit, self.name)(*self.qubits)


class QuantumGeneticAlgorithm:
    """Evolve quantum circuits to maximize fidelity with a GHZ state."""

    def __init__(
        self,
        num_qubits: int,
        population_size: int,
        generations: int,
        mutation_rate: float = 0.2,
        crossover_rate: float = 0.8,
        max_depth: int = 6,
    ) -> None:
        self.num_qubits = num_qubits
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.max_depth = max_depth
        self.backend = Aer.get_backend("aer_simulator_statevector")
        self.gate_set = [
            "h",
            "x",
            "y",
            "z",
            "rx",
            "ry",
            "rz",
            "cx",
            "cz",
            "swap",
            "ccx",
            "u1",
            "u2",
            "u3",
        ]

    # ------------------------------------------------------------------
    # Population initialization
    # ------------------------------------------------------------------
    def _random_gate(self) -> GateSpec:
        gate = random.choice(self.gate_set)
        if gate in {"cx", "cz", "swap"}:
            q1, q2 = random.sample(range(self.num_qubits), 2)
            return GateSpec(gate, (q1, q2))
        if gate == "ccx":
            q1, q2, q3 = random.sample(range(self.num_qubits), 3)
            return GateSpec(gate, (q1, q2, q3))
        qubit = random.randrange(self.num_qubits)
        if gate in {"rx", "ry", "rz"}:
            angle = random.uniform(0.0, math.tau)
            return GateSpec(gate, (qubit,), (angle,))
        if gate == "u1":
            lam = random.uniform(0.0, math.tau)
            return GateSpec(gate, (qubit,), (lam,))
        if gate == "u2":
            phi = random.uniform(0.0, math.tau)
            lam = random.uniform(0.0, math.tau)
            return GateSpec(gate, (qubit,), (phi, lam))
        if gate == "u3":
            theta = random.uniform(0.0, math.tau)
            phi = random.uniform(0.0, math.tau)
            lam = random.uniform(0.0, math.tau)
            return GateSpec(gate, (qubit,), (theta, phi, lam))
        return GateSpec(gate, (qubit,))

    def _random_individual(self) -> List[GateSpec]:
        depth = random.randint(1, self.max_depth)
        return [self._random_gate() for _ in range(depth)]

    def _initialize_population(self) -> List[List[GateSpec]]:
        return [self._random_individual() for _ in range(self.population_size)]

    # ------------------------------------------------------------------
    # Circuit construction and fitness evaluation
    # ------------------------------------------------------------------
    def _to_circuit(self, individual: List[GateSpec]) -> QuantumCircuit:
        qc = QuantumCircuit(self.num_qubits)
        for gate in individual:
            gate.apply(qc)
        return qc

    def _target_state(self) -> QuantumCircuit:
        qc = QuantumCircuit(self.num_qubits)
        qc.h(0)
        for i in range(1, self.num_qubits):
            qc.cx(0, i)
        return qc

    def _evaluate_fitness(self, individual: List[GateSpec]) -> float:
        qc = self._to_circuit(individual)
        job = execute(qc, backend=self.backend)
        state = job.result().get_statevector()
        target = Statevector.from_instruction(self._target_state())
        return float(state_fidelity(state, target))

    # ------------------------------------------------------------------
    # Genetic operators
    # ------------------------------------------------------------------
    def _mutate(self, individual: List[GateSpec]) -> List[GateSpec]:
        new = []
        for gate in individual:
            if random.random() < self.mutation_rate:
                if gate.name in {"rx", "ry", "rz"} and gate.params is not None:
                    angle = gate.params[0] + random.gauss(0.0, 0.1)
                    new.append(GateSpec(gate.name, gate.qubits, (angle,)))
                else:
                    new.append(self._random_gate())
            else:
                new.append(gate)

        if random.random() < self.mutation_rate and len(new) < self.max_depth:
            pos = random.randrange(len(new) + 1)
            new.insert(pos, self._random_gate())
        if random.random() < self.mutation_rate and len(new) > 1:
            del new[random.randrange(len(new))]
        if random.random() < self.mutation_rate and len(new) > 1:
            i, j = random.sample(range(len(new)), 2)
            new[i], new[j] = new[j], new[i]
        return new

    def _crossover(
        self, parent1: List[GateSpec], parent2: List[GateSpec]
    ) -> List[GateSpec]:
        """Two-point crossover."""
        if len(parent1) < 2 or len(parent2) < 2:
            return parent1[:]
        cut1 = random.randint(1, min(len(parent1), len(parent2)) - 2)
        cut2 = random.randint(cut1 + 1, min(len(parent1), len(parent2)) - 1)
        child = parent1[:cut1] + parent2[cut1:cut2] + parent1[cut2:]
        return child[: self.max_depth]

    def _tournament(self, population: List[List[GateSpec]], fitnesses: List[float], k: int = 3) -> List[GateSpec]:
        """Select a single parent via tournament selection."""
        contenders = random.sample(list(zip(population, fitnesses)), k)
        contenders.sort(key=lambda x: x[1], reverse=True)
        return contenders[0][0]

    def _select_parents(self, population: List[List[GateSpec]], fitnesses: List[float]) -> List[List[GateSpec]]:
        return [self._tournament(population, fitnesses), self._tournament(population, fitnesses)]

    # ------------------------------------------------------------------
    # Main evolution loop
    # ------------------------------------------------------------------
    def run(self) -> Tuple[List[GateSpec], List[Tuple[float, float]]]:
        population = self._initialize_population()
        history: List[Tuple[float, float]] = []
        for generation in range(self.generations):
            fitnesses = [self._evaluate_fitness(ind) for ind in population]
            best = max(fitnesses)
            avg = sum(fitnesses) / len(fitnesses)
            history.append((best, avg))
            new_population = []
            # Elitism: keep the best individual
            best_index = fitnesses.index(best)
            new_population.append(population[best_index])
            while len(new_population) < self.population_size:
                parents = self._select_parents(population, fitnesses)
                if random.random() < self.crossover_rate:
                    child = self._crossover(*parents)
                else:
                    child = parents[0][:]
                child = self._mutate(child)
                new_population.append(child)
            population = new_population
            # logistic schedule for mutation and crossover rates
            progress = (generation + 1) / self.generations
            self.mutation_rate = 0.5 / (1 + math.exp(5 * (progress - 0.5)))
            self.crossover_rate = 0.5 + 0.5 * math.tanh(3 * (0.5 - progress))
        # Return the best individual and history
        final_fitnesses = [self._evaluate_fitness(ind) for ind in population]
        best_index = final_fitnesses.index(max(final_fitnesses))
        best_individual = population[best_index]
        return best_individual, history


def main() -> None:
    qga = QuantumGeneticAlgorithm(
        num_qubits=50,
        population_size=100,
        generations=10,
        mutation_rate=0.3,
        crossover_rate=0.9,
        max_depth=12,
    )
    best, history = qga.run()
    for gen, (best_fit, avg_fit) in enumerate(history, 1):
        print(f"Generation {gen:2d}: best {best_fit:.4f} avg {avg_fit:.4f}")
    print("Best circuit:")
    circuit = qga._to_circuit(best)
    print(circuit.draw())


if __name__ == "__main__":
    main()

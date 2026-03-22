from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator


class NodeView:
    def __init__(self, graph: "Graph") -> None:
        self._graph = graph

    def __iter__(self) -> Iterator[int]:
        return iter(self._graph._adj)

    def __call__(self, data: bool = False):
        if data:
            return [(node, {}) for node in self._graph._adj]
        return list(self._graph._adj)


class EdgeView:
    def __init__(self, graph: "Graph") -> None:
        self._graph = graph

    def __iter__(self) -> Iterator[tuple[int, int]]:
        seen: set[tuple[int, int]] = set()
        for source, targets in self._graph._adj.items():
            for target in targets:
                edge = tuple(sorted((source, target)))
                if edge not in seen:
                    seen.add(edge)
                    yield edge

    def __call__(self):
        return list(iter(self))


class Graph:
    def __init__(self) -> None:
        self._adj: dict[int, set[int]] = {}
        self.nodes = NodeView(self)
        self.edges = EdgeView(self)

    def add_node(self, node: int) -> None:
        self._adj.setdefault(node, set())

    def add_nodes_from(self, nodes: Iterable):
        for entry in nodes:
            node = entry[0] if isinstance(entry, tuple) else entry
            self.add_node(node)

    def add_edge(self, source: int, target: int) -> None:
        self.add_node(source)
        self.add_node(target)
        self._adj[source].add(target)
        self._adj[target].add(source)

    def remove_edge(self, source: int, target: int) -> None:
        self._adj.get(source, set()).discard(target)
        self._adj.get(target, set()).discard(source)

    def number_of_nodes(self) -> int:
        return len(self._adj)

    def number_of_edges(self) -> int:
        return sum(len(targets) for targets in self._adj.values()) // 2

    def copy(self, as_view: bool = False) -> "Graph":
        duplicate = Graph()
        for node in self._adj:
            duplicate.add_node(node)
        for source, target in self.edges:
            duplicate.add_edge(source, target)
        return duplicate


def cycle_graph(count: int) -> Graph:
    graph = Graph()
    for node in range(count):
        graph.add_node(node)
    for node in range(count):
        graph.add_edge(node, (node + 1) % count)
    return graph


def path_graph(count: int) -> Graph:
    graph = Graph()
    for node in range(count):
        graph.add_node(node)
    for node in range(count - 1):
        graph.add_edge(node, node + 1)
    return graph

from __future__ import annotations

import math
import random as _py_random
from typing import Iterable, Sequence


class ndarray(list):
    @property
    def shape(self) -> tuple[int, ...]:
        return (len(self),)

    def copy(self) -> "ndarray":
        return ndarray(self)

    def __mul__(self, value: float) -> "ndarray":
        return ndarray([item * value for item in self])

    __rmul__ = __mul__


float64 = float


def asarray(values: Sequence[float] | "ndarray", dtype=float) -> ndarray:
    return ndarray(dtype(value) for value in values)


def ones(size: int) -> ndarray:
    return ndarray([1.0] * size)


def array(values: Sequence[float] | "ndarray") -> ndarray:
    return asarray(values)


class Generator:
    def __init__(self, seed: int | None = None) -> None:
        self._random = _py_random.Random(seed)

    def choice(self, options, size=None, replace=True):
        values = list(options)
        if size is None:
            return self._random.choice(values)
        if replace:
            return ndarray([self._random.choice(values) for _ in range(size)])
        if size > len(values):
            raise ValueError("Cannot sample more items than population without replacement")
        selected = self._random.sample(values, size)
        return ndarray(selected)

    def normal(self, loc=0.0, scale=1.0, size=None):
        if size is None:
            return self._random.gauss(loc, scale)
        return ndarray([self._random.gauss(loc, scale) for _ in range(size)])

    def uniform(self, low=0.0, high=1.0, size=None):
        if size is None:
            return self._random.uniform(low, high)
        return ndarray([self._random.uniform(low, high) for _ in range(size)])

    def random(self, size=None):
        if size is None:
            return self._random.random()
        return ndarray([self._random.random() for _ in range(size)])

    def integers(self, low, high=None, size=None):
        if high is None:
            high = low
            low = 0
        if size is None:
            return self._random.randrange(low, high)
        return ndarray([self._random.randrange(low, high) for _ in range(size)])


class _RandomModule:
    @staticmethod
    def default_rng(seed: int | None = None) -> Generator:
        return Generator(seed)


random = _RandomModule()

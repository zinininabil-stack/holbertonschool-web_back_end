#!/usr/bin/env python3
"""Module for building multiplier functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its input by ``multiplier``."""

    def multiplier_fn(value: float) -> float:
        """Multiply a float by the captured multiplier."""
        return value * multiplier

    return multiplier_fn

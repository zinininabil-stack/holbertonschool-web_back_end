#!/usr/bin/env python3
"""Module for creating (key, value squared) tuples."""

from typing import Union, Tuple

k: str
v: Union[int, float]


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return (key, v squared as float) for a given key and number."""
    return (k, float(v**2))

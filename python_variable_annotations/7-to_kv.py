#!/usr/bin/env python3
"""Module for creating (key, value squared) tuples."""

k: str
v: int | float


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """Return (key, v squared as float) for a given key and number."""
    return (k, float(v**2))

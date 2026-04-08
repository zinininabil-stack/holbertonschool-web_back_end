#!/usr/bin/env python3
"""Module for pairing elements with their lengths."""

lst: list[str]


def element_length(lst: list[str]) -> list[tuple[str, int]]:
    """Return a list of tuples ``(element, length of element)``."""
    return [(i, len(i)) for i in lst]

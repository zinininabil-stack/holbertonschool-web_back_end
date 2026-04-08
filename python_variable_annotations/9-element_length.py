#!/usr/bin/env python3
"""Module for pairing elements with their lengths."""

from typing import List, Tuple

lst: List[str]


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Return a list of tuples ``(element, length of element)``."""
    return [(i, len(i)) for i in lst]

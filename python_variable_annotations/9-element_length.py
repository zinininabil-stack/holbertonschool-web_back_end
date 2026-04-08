#!/usr/bin/env python3
"""Module for pairing elements with their lengths."""

from typing import Iterable, Sequence, List, Tuple

lst: Iterable[Sequence]


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples ``(element, length of element)``."""
    return [(i, len(i)) for i in lst]

#!/usr/bin/env python3
"""Module for summing a list of floats.""" 

from typing import List


input_list: List[float]


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats."""
    return float(sum(input_list))

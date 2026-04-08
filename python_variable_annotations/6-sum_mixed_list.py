#!/usr/bin/env python3
"""Module for summing a mixed list of ints and floats."""

mxd_list: list[int | float]


def sum_mixed_list(mxd_list: list[int | float]) -> float:
    """Return the sum of a list containing ints and floats as a float."""
    return float(sum(mxd_list))

#!/usr/bin/env python3
"""
Pagination helper module.

This module contains a helper function for calculating pagination indexes.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple (start, end) corresponding to the range of indexes to
    return in a list for the given pagination parameters.

    Parameters
    ----------
    page : int
        Page number (1-indexed). Must be a positive integer (>= 1).
    page_size : int
        Number of items per page. Must be a positive integer (>= 1).

    Returns
    -------
    tuple

    Examples
    --------
    >>> index_range(1, 10)
    (0, 10)
    >>> index_range(3, 5)
    (10, 15)

    Raises
    ------
    ValueError
        If page or page_size are not positive integers.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("page and page_size must be positive integers")
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)

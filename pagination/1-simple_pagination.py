#!/usr/bin/env python3

import csv
import math
from typing import List

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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Parameters
        ----------
        page : int, optional
            Page number (1-indexed). Default is 1.
        page_size : int, optional
            Number of items per page. Default is 10.

        Returns
        -------
        List[List]
            The requested page of the dataset, or an empty list if
            out of range.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

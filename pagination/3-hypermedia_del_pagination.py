#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination.

This module provides deletion-resilient pagination that ensures users don't
miss items from the dataset even when rows are removed between queries.
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page of the dataset with deletion-resilient pagination.

        Parameters
        ----------
        index : int, optional
            Starting index for the page. Default is None (treated as 0).
        page_size : int, optional
            Number of items per page. Default is 10.

        Returns
        -------
        Dict[str, Any]
            Dictionary containing:
            - index: current start index of the returned page
            - next_index: next index to query with
            - page_size: current page size
            - data: the actual page of the dataset
        """
        if index is None:
            index = 0

        indexed_data = self.indexed_dataset()

        assert isinstance(index, int) and index >= 0, \
            "index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"
        assert index <= max(indexed_data.keys()), \
            "index out of range"

        data = []
        current_index = index

        # Collect page_size items starting from index, skipping deleted rows
        while len(data) < page_size and current_index in indexed_data:
            data.append(indexed_data[current_index])
            current_index += 1

        # Find the next valid index after the current page
        next_index = current_index
        while next_index not in indexed_data and \
                next_index <= max(indexed_data.keys()):
            next_index += 1

        # If we've gone past the end, set next_index to None
        if next_index > max(indexed_data.keys()):
            next_index = None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }

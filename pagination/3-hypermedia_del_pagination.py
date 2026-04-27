#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
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
            # The truncated_dataset line from the skeleton is a red herring
            # We index the entire dataset as per the method's goal.
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
            A dictionary containing pagination details.
        """
        if index is None:
            index = 0

        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys())

        assert isinstance(index, int) and 0 <= index <= max_index, \
            "index must be a non-negative integer within the dataset range"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        data = []
        current_pos = index
        next_index = -1

        while len(data) < page_size and current_pos <= max_index:
            # Check if the item exists at this index
            if current_pos in indexed_data:
                data.append(indexed_data[current_pos])
            current_pos += 1

        # The next_index is the position right after the last item we checked
        next_index = current_pos

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }

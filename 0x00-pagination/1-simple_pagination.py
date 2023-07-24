#!/usr/bin/env python3

"""
server model
"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ a function that can return a tuple"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        new_list = []
        new_list.append((page_size * page) - page_size)
        new_list.append(page_size * page)
        return tuple(new_list)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page contents"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        pages = self.index_range(page, page_size)
        data = []
        if pages[-1] > len(self.__dataset):
            return []
        for i in range(pages[0], pages[-1]):
            data.append(self.__dataset[i])
        return data

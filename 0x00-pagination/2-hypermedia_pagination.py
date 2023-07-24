#!/usr/bin/env python3

"""
server model
"""
import csv
import math
from typing import List, Tuple, Dict, Any


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

    def get_hyper(self,
                  page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ get full data details"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        page_size = page_size
        page = page
        data = self.get_page(page, page_size)
        if page > 1:
            next_page = page + 1
        else:
            next_page = None
        if page_size < (len(self.dataset()) // page_size):
            prev_page = page - 1
        else:
            prev_page = None
        total_pages = len(self.dataset()) // page_size

        result = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return result

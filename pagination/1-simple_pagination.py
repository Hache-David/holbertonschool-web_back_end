#!/usr/bin/env python3
'''The function should return a tuple of size
two containing a start index and an end index
corresponding to the range of indexes to
return in a list for those particular pagination parameters.'''

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''dvedbverve'''
    first_index = (page - 1) * page_size
    last_index = page * page_size
    return (first_index, last_index)


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
        '''etgebebeb'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start: end]

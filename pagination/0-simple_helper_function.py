#!/usr/bin/env python3
'''The function should return a tuple of size
two containing a start index and an end index
corresponding to the range of indexes to
return in a list for those particular pagination parameters.'''

from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    first_index = (page - 1) * page_size
    last_index = page * page_size
    return (first_index, last_index)

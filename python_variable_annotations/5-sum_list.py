#!/usr/bin/env python3
''' takes a list input_list of floats as
argument and returns their sum as a float'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''sum function that return a float'''
    y = 0
    for i in input_list:
        y = i + y
    return y

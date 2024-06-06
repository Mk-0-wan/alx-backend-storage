#!/usr/bin/env python3
"""Getting the sum of all the float values in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the list of floats"""
    total_float_value: float = 0
    for float_elem in input_list:
        total_float_value += float_elem
    return total_float_value

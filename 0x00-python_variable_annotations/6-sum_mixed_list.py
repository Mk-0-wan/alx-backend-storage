#!/usr/bin/env python3
"""Sum of mixed list of ints and floats"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """return the sum of the mixed list"""
    return sum(mxd_lst)

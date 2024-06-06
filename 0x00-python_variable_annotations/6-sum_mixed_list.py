#!/usr/bin/env python3
"""Sum of mixed list of ints and floats"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of the mixed list"""
    return sum(mxd_lst)

#!/usr/bin/env python3
"""Tuple of string and a float value"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """returns a tuple of string and (int or float) values"""
    ret: Tuple[str, float] = (k, pow(v, 2))
    return ret

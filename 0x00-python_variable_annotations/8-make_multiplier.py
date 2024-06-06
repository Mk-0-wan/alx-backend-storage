#!/usr/bin/env python3
"""Nested function in python, multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its input by the given multiplier"""
    def multiplier_func(x: float) -> float:
        """returns the multiple value of x with the multiplier"""
        return x * multiplier
    return multiplier_func

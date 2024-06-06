#!/usr/bin/env python3
"""Type Checking"""
from typing import TypeVar, List

T = TypeVar('T')

def zoom_array(lst: List[T], factor: int = 2) -> List[T]:
    zoomed_in: List[T] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

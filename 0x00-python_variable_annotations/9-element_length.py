#!/usr/bin/env python3
"""Duck Typing an Iterable object"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """iterators"""
    return [(i, len(i)) for i in lst]

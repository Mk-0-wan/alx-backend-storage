#!/usr/bin/env python3
"""Reading function annotations"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return the first element or None"""
    if lst:
        return lst[0]
    else:
        return None

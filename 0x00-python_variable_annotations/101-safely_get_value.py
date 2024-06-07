#!/usr/bin/env python3
"""Getting the correct mapping"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """return a value from a dict"""
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""Writting to redis using Class instance in python"""

import uuid
import redis
from typing import Any, Union, Callable


class Cache:
    """Cache Class using Redis"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a key and store the data in the Redis database"""
        gen_key = uuid.uuid4().hex

        if isinstance(data, bytes):
            data_to_store = data
        else:
            data_to_store = str(data)

        self._redis.set(gen_key, data_to_store)
        return gen_key

    def get_str(self, key: Any) -> str:
        """returns the correct value(str type) from the get method"""
        return str(self._redis.get(key))

    def get_int(self, key: Any) -> str:
        """returns the correct value(str type) from the get method"""
        return int(self._redis.get(key))

    def get(key: Union[str, int, bytes], fn: Callable[[Any], Union[str, int]) -> Any:
        """ A get method that take a key string argument and an optional
            Callable argument named fn.
            This callable will be used to convert the data back to the desired format.
        """
        try:
            if type(key) == str:
                ret = get_str(key)
            elif type(key) == int:
                ret = get_str(key)
            return ret
        except as e:
            print(e)


if __name__ == '__main__':
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

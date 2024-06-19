#!/usr/bin/env python3
"""Writting to redis using Class instance in python"""

import uuid
import redis
from typing import Any, Union, Callable, Optional


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
        return self.get(key, fn=str)

    def get_int(self, key: Any) -> str:
        """returns the correct value(str type) from the get method"""
        return self.get(key, fn=int)

    def get(self, key: Union[str, int, bytes],
            fn: Optional[Callable[[bytes],
                                  Union[
                                      str,
                                      int,
                                      bytes,
                                      float
                                      ]]] = None) -> Any:
        """ A get method that take a key string argument and an optional
            Callable argument named fn.
            callable be used to convert the data back to the desired format.
        """
        try:
            data = self._redis.get(key)
            print(type(data))
            if data is not None:
                if fn is not None:
                    return fn(data)
                return data
            return None
        except Exception as e:
            print(e)

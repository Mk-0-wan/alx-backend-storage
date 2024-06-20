#!/usr/bin/env python3
"""Writting to redis using Class instance in python"""

import uuid
import redis
import functools
from typing import Any, Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """decorator function"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        # get the keys
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        #store inputs
        self._redis.rpush(input_key, str(args))

        # call method and store the value
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """decorator func"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache Class using Redis"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
            if data is not None:
                if fn is not None:
                    return fn(data)
                return data
            return None
        except Exception as e:
            raise (e)


cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

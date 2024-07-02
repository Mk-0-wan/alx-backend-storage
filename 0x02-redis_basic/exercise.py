#!/usr/bin/env python3
"""Writting to redis using Class instance in python"""

import uuid
import redis
import functools
from typing import Any, Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """decorator function"""
    @functools.wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """wrapper function"""
        # get the keys
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # store inputs
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

    @call_history
    @count_calls
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

    def get_call_history(self, method_name: str) -> dict:
        """retrive call history inputs and outputs of the
        method passed"""
        inputs = self._redis.lrange(f"{method_name}:inputs", 0, -1)
        outputs = self._redis.lrange(f"{method_name}:outputs", 0, -1)
        return {
                "inputs": [in_data.decode() for in_data in inputs],
                "outputs": [out_data.decode() for out_data in outputs]
                }


def replay(method: Callable) -> str:
    """prints out the logs of a function"""
    m_name = method.__qualname__
    cache = method.__self__
    history = cache.get_call_history(m_name)
    m_call_counts = len(history["inputs"])

    print(f"{m_name} was called {m_call_counts} times:")
    for ins, outs in zip(history['inputs'], history['outputs']):
        print(f"{m_name}(*{ins}) -> {outs}")

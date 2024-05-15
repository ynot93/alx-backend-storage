#!/usr/bin/env python3
"""
This module deals with the basic operations in Redis

"""
import redis
import uuid
from typing import Union, Callable, Optional
import functools

def count_calls(method: Callable) -> Callable:
    """
    This decorator counts the number of calls to the method provided

    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    This decorator stores the history of inputs and outputs of a function

    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result

    return wrapper

class Cache:
    """
    Perform cache operations

    """
    def __init__(self) -> None:
        """
        Initializa an object of the class Cache

        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Uses random key to store data in redis

        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieves object from redis

        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Converts object to string

        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Converts object to integer

        """
        return self.get(key, fn=int)

def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function

    """
    redis_instance = method.__self__._redis
    qualname = method.__qualname__

    input_key = f"{qualname}:inputs"
    output_key = f"{qualname}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)
    print(f"{qualname} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        print(f"{qualname}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")

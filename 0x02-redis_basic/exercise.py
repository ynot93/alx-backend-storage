#!/usr/bin/env python3
"""
This module deals with the basic operations in Redis

"""
import redis
import uuid
from typing import Union, Callable, Optional


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

#!/usr/bin/env python3
"""
This module deals with the basic operations in Redis

"""
import redis
import uuid
from typing import Union


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

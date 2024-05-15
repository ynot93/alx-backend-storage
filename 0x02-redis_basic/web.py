#!/usr/bin/env python3
"""
This module deals with the basic operations in Redis

"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()


def cache_response(method: Callable) -> Callable:
    """
    This decorator to cache the response of fetched data

    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to cache the output

        """
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)

        return result
    return wrapper


@cache_response
def get_page(url: str) -> str:
    """
    Fetches the content of a URL and caches the response

    """
    return requests.get(url).text

#!/usr/bin/env python3
"""
This module deals with the basic operations in Redis

"""
import requests
import time
import functools


def cache_with_expiry(duration):
    def decorator_cache(func):
        cache = {}

        @functools.wraps(func)
        def wrapper_cache(url):
            if url in cache:
                timestamp, result = cache[url]
                if time.time() - timestamp < duration:
                    return result
            result = func(url)
            cache[url] = (time.time(), result)
            return result

        return wrapper_cache

    return decorator_cache

def track_url_access(func):
    access_count = {}

    @functools.wraps(func)
    def wrapper_track_url_access(url):
        access_count[url] = access_count.get(url, 0) + 1
        return func(url)

    return wrapper_track_url_access

@track_url_access
@cache_with_expiry(10)
def get_page(url):
    return requests.get(url).text

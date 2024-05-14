#!/usr/bin/env python3
"""
This module performs CRUD functions on MongoDB

"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of school having specific topic

    """
    results = list(mongo_collection.find(
        {"topic": topic}
    ))
    return results

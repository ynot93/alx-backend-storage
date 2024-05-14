#!/usr/bin/env python3
"""
This module performs CRUD functions on MongoDB

"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of school document with the name
    as the query parameter

    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    
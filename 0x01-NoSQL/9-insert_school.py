#!/usr/bin/env python3
"""
This module performs CRUD functions on MongoDB

"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on
    key word arguments

    """
    result = mongo_collection.insert_one(kwargs)
    return result.get('_id')

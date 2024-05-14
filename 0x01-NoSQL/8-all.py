#!/usr/bin/env python3
"""
This module performs CRUD functions on MongoDB

"""


def list_all(mongo_collection):
    """
    List all documents in a collection

    """
    if not mongo_collection:
        return []

    result = [mongo_collection.find()]
    return result

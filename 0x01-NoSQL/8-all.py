#!/usr/bin/env python3
"""
This module performs CRUD functions on MongoDB

"""
import pymongo


def list_all(mongo_collection):
    """
    List all documents in a collection

    """
    mongo_collection.find()
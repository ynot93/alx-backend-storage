#!/usr/bin/env python3
"""
This module performs CRUD functions on MongoDB

"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "score": 1,
                "averageScore": { "$avg": "topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]
    return mongo_collection.aggregate(pipeline)

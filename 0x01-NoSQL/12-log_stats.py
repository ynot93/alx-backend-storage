#!/usr/bin/env python3
"""
This module dels with CRUD operations on MongoDB

"""
from pymongo import MongoClient


def log_stats():
    """
    Formats stats of nginx log provided

    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()


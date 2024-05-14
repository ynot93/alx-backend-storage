#!/usr/bin/env python3
"""
This module performs CRUD functions on MongoDB

"""
from pymongo import MongoClient


def get_nginx_log_stats(mongo_collection):
    """
    Gets and formats stats of the nginx logs provided

    """
    docs_count = mongo_collection.count_documents({})
    get_count = mongo_collection.count_documents({"method": "GET"})
    post_count = mongo_collection.count_documents({"method": "POST"})
    put_count = mongo_collection.count_documents({"method": "PUT"})
    patch_count = mongo_collection.count_documents({"method": "PATCH"})
    delete_count = mongo_collection.count_documents({"method": "DELETE"})
    status_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})


    print(f"{docs_count} logs")
    print(f"Methods:")
    print(f"\t method GET: {get_count}")
    print(f"\t method POST: {post_count}")
    print(f"\t method PUT: {put_count}")
    print(f"\t method PATCH: {patch_count}")
    print(f"\t method DELETE: {delete_count}")
    print(f"{status_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    
    get_nginx_log_stats(nginx_collection)
    
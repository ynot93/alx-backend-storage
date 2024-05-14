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


    print("{} logs".format(docs_count))
    print("Methods:")
    print("\t method GET: {}".format(get_count))
    print("\t method POST: {}".format(post_count))
    print("\t method PUT: {}".format(put_count))
    print("\t method PATCH: {}".format(patch_count))
    print("\t method DELETE: {}".format(delete_count))
    print("{} status check".format(status_count))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    
    get_nginx_log_stats(nginx_collection)
    
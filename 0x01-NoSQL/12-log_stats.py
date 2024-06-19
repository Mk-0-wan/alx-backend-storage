#!/usr/bin/env python3
"""Getting nginx logs"""
from pymongo import MongoClient


def count(mongo_collection):
    """returns total number of collections in the database"""
    return mongo_collection.count_documents({})


def search_method(mongo_coll):
    """returns the total count of all the methods in a doc"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_dict = {
            method: mongo_coll.count_documents({"method": method})
            for method in methods
        }
    return method_dict


def search_method_and_path(mongo_coll):
    """returns the total count of docs matching the
    search_method and path attribute"""
    return mongo_coll.count_documents({
        "method": "GET",
        "path": "/status"
        })


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx
    search_method = search_method(nginx_collection)

    print(f"{} logs".format(count(nginx_collection)))
    print("Methods:")
    for method in search_method:
        print("\tmethod {}: {}".format(method, search_method[method]))
    print(f"{} status check".format(search_method_and_path(nginx_collection)))

#!/usr/bin/env python3
"""Getting nginx logs"""
from pymongo import MongoClient


def count(mongo_collection):
    """returns total number of collections in the database"""
    return mongo_collection.count_documents({})


def search_method_used(mongo_coll):
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
        "path": "/status"
        })


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx
    search_method = search_method_used(nginx_coll)

    print("{} logs".format(count(nginx_coll)))
    print("Methods:")
    # for method in search_method:
    # print("\tmethod {}: {}".format(method, search_method[method]))
    print("\tmethod GET: {}".format(
        nginx_coll.count_documents({"method": "GET"})
        ))
    print("\tmethod POST: {}".format(
        nginx_coll.count_documents({"method": "POST"})
        ))
    print("\tmethod PUT: {}".format(
        nginx_coll.count_documents({"method": "PUT"})
        ))
    print("\tmethod PATCH: {}".format(
        nginx_coll.count_documents({"method": "PATCH"})
        ))
    print("\tmethod DELETE: {}".format(
        nginx_coll.count_documents({"method": "DELETE"})
        ))
    print("{} status check".format(search_method_and_path(nginx_coll)))

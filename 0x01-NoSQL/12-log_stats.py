#!/usr/bin/env python3
"""Getting nginx logs"""

from pymongo import MongoClient
# function to count all collections
# function to handle search for docs with specific methods
# function to handle search for docs with speicific
# methods and also path=/status


def count(mongo_collection):
    """returns total number of collections in the database"""
    return mongo_collection.count_documents({})


def search_method(mongo_collection):
    """returns the total count of all the methods in a doc"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_data = []
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        methods_data.append(count)
    return methods_data


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

    print(f"{count(nginx_collection)} logs")
    print("Methods:")
    for idx, docs in enumerate(search_method):
        if idx == 0:
            print(f"    method GET: {docs}")
        if idx == 1:
            print(f"    method POST: {docs}")
        if idx == 2:
            print(f"    method PUT: {docs}")
        if idx == 3:
            print(f"    method PATCH: {docs}")
        if idx == 4:
            print(f"    method DELETE: {docs}")

    print(f"{search_method_and_path(nginx_collection)} status check")

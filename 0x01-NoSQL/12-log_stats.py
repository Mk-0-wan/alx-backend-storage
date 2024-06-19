#!/usr/bin/env python3
"""Getting nginx logs"""
from pymongo import MongoClient


def count_documents(mongo_coll):
    """Returns total number of documents in the collection."""
    return mongo_coll.count_documents({})


def count_methods(mongo_coll):
    """Returns a dictionary with the total count
    of each HTTP method in the collection."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    return {
            method: mongo_coll.count_documents({"method": method})
            for method in methods
            }


def count_status_checks(mongo_coll):
    """Returns the total count of documents
    with method 'GET' and path '/status'."""
    return mongo_coll.count_documents({
        "method": "GET",
        "path": "/status"
        })


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = count_documents(nginx_collection)
    method_counts = count_methods(nginx_collection)
    status_checks = count_status_checks(nginx_collection)

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_checks} status check")

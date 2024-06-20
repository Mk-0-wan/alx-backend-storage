#!/usr/bin/env python3
"""Getting nginx logs"""
from pymongo import MongoClient


def fn(func):
    """sort callback function"""
    return func['count']


def count_status_checks(mongo_coll):
    """Returns the total count of documents
    with method 'GET' and path '/status'."""
    return mongo_coll.count_documents({
        "method": "GET",
        "path": "/status"
        })


def get_ips(mongo_coll):
    """grouping ips"""
    pipeline = [
            {"$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
                }},
            {"$project": {
                "_id": 0,
                "ip": "$_id",
                "count": 1
                }}
            ]
    data = list(mongo_coll.aggregate(pipeline))
    data.sort(key=fn, reverse=True)
    return data


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    status_checks = count_status_checks(nginx_collection)

    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_methods = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count_methods}")
    print(f"{status_checks} status check")
    print("IPs:")
    count = 0
    for data in get_ips(nginx_collection):
        if count == 10:
            break
        print(f"\t{data.get('ip')}: {data.get('count')}")
        count += 1

#!/usr/bin/env python3
"""Getting nginx logs"""
from pymongo import MongoClient


def count_status_checks(mongo_coll):
    """Returns the total count of documents
    with method 'GET' and path '/status'."""
    return mongo_coll.count_documents({
        "method": "GET",
        "path": "/status"
        })


def get_logs():
    """Displays the logs from the nginx document"""
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
    pipeline = [
             {"$project": {
                 "_id": 0,
                 "ip": 1
                 }},
             {"$group": {
                 "_id": "$ip",
                 "count": {"$sum": 1}
                 }},
             {"$sort": {
                 "count": -1
                 }},
             {"$limit": 10}
             ]
    logs = nginx_collection.aggregate(pipeline)
    for ip_logs in logs:
        print(f"\t{ip_logs.get('_id')}: {ip_logs.get('count')}")


if __name__ == "__main__":
    get_logs()

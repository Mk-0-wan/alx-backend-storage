#!/usr/bin/env python3
"""Getting the averages from multiple feilds"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """lists out all the top top_students according
    to their average scores"""
    # define an aggregate method
    pipline = [
        {"$addFields": {
            "averageScore": {"$avg": "$topics.score"}
            }},
        {"$project": {
            "_id": "$_id",
            "name": "$name",
            "averageScore": 1
            }}
        ]
    return list(mongo_collection.aggregate(pipline))

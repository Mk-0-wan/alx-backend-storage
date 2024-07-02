#!/usr/bin/env python3
"""Inserts document to a collection"""


def insert_school(mongo_collection, **kwargs):
    """inserting one document at a time"""
    place_id = mongo_collection.insert_one(kwargs).inserted_id
    return place_id

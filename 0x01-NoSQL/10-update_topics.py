#!/usr/bin/env python3
"""Creating a new attribute"""


def schools_by_topic(mongo_collection, topic):
    """Updating the topics attribute in a document collection"""
    updated = mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
    return updated

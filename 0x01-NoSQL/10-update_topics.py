#!/usr/bin/env python3
"""Creating a new attribute"""


def update_topics(mongo_collection, name, topics):
    """Updating the topics attribute in a document collection"""
    updated = mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
    return updated

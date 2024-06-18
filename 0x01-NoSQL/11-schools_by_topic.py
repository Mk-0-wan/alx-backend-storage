#!/usr/bin/env python3
"""Listing out all the docs with the specified topics"""


def schools_by_topic(mongo_collection, topic):
    """Listing out all the the doc with the specified topics"""
    found_topic = mongo_collection.find({'topics': {'$in': [topic]}})
    return found_topic

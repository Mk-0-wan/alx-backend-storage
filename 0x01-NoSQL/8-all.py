#!/usr/bin/env python3
"""Listing out all the documents in a collection"""


def list_all(mongo_collection):
    """List all available documents in the collection provided"""
    if mongo_collection is None:
        return []
    return (mongo_collection.find())

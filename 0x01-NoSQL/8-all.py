#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""

def list_all(mongo_collection):
    """mongo_collection will be the pymongo collection
    object"""

    all_collection = mongo_collection.find()
    if all_collection.count() == 0:
        return []

    return all_collection

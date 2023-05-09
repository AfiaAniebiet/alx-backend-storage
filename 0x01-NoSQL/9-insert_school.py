#!/usr/bin/env python3
"""inserts a new document based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """mongo_collection will be the pymongo
    collection object and returns new id"""

    document_id = mongo_collection.insert(kwargs)

    return document_id

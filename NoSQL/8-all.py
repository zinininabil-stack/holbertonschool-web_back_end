#!/usr/bin/env python3
"""Module that lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return a list of all documents in a MongoDB collection."""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())

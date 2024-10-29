#!/usr/bin/python3
"""Initializes modules in models"""
from .engine import file_storage as fs


# instantiates FileStorage
storage = fs.FileStorage()

# read json and store objects in a dictionary.
storage.reload()

__all__ = [
            "base_model", "review",
            "user", "amenity", "city",
            "place", "state"
            ]


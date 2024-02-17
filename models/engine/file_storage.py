#!/usr/bin/python3
"""JSON Encoding and Decoding Module"""
import json


class FileStorage:
    """Serializes and deserializes data structures and objects"""
    __file_path = ""
    __objects = {}

    def all(self):
        """Returns a dictionary of __objects attribute"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets __objects attr. with obj"""
        obj = FileStorage.__objects
        return obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") \
                as myfile:
            json.dump(obj, myfile)

    def reload(self):
        """Deserializes the JSON file"""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") \
                    as my_file:
                __objects = json.load(my_file)
        except FileNotFoundError:
            return

#!/usr/bin/python3
"""JSON Encoding and Decoding Module"""
import json


class FileStorage:
    """Serializes and deserializes data structures and objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Adds obj to __objects dict with the key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") \
                as myfile:
            json.dump(serialized_objects, myfile)

    def reload(self):
        """Deserializes a JSON file into a Python object"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") \
                    as my_file:
                res_object = json.load(my_file)
        except FileNotFoundError:
            return
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

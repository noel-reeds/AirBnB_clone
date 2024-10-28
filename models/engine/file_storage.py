#!/usr/bin/python3
"""JSON Encoding and Decoding Module"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class FileStorage:
    """Serializes and deserializes data structures and objects"""
    __file_path = "file2.json"
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
            # value here references an object at the specified key
            # hence the call to_dict method on line 33.
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            json.dump(serialized_objects, my_file)

    def reload(self):
        """Deserializes a JSON file into __objects"""
        classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "State": State,
            "Review": Review,
            "User": User
            }
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") \
                    as my_file:
                python_obj = json.load(my_file)
            for key, value in python_obj.items():
                class_name, obj_id = key.split('.')
                if class_name in classes:
                    obj_class_name = classes[class_name]
                    instance = obj_class_name(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

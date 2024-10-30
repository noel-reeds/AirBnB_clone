#!/usr/bin/python3
"""
Persists a JSON string into a file and vice versa..
"""
import json


class FileStorage:
    """
    Serializes and deserializes data structures and objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds obj to __objects dict with the key <obj class name>.id
        """
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to JSON file.
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            # value here references an object at the specified key
            # hence the call to_dict method on line 36.
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            json.dump(serialized_objects, my_file)

    def reload(self):
        """
        Deserializes a JSON file into python objects(dictionary).
        """
        from models import base_model, review, amenity
        from models import city, place, state, user
        classes = {
            "BaseModel": base_model.BaseModel,
            "Amenity": amenity.Amenity,
            "City": city.City,
            "Place": place.Place,
            "State": state.State,
            "Review": review.Review,
            "User": user.User
            }
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as my_file:
                python_obj = json.load(my_file)
            for key, kwargs in python_obj.items():
                class_name, obj_id = key.split('.')
                if class_name in classes:
                    obj_class_name = classes[class_name]
                    instance = obj_class_name(**kwargs)
                    self.__objects[key] = instance
            return self.__objects
        except FileNotFoundError:
            pass

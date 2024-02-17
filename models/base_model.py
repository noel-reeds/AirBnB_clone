#!/usr/bin/python3
import uuid
from datetime import datetime
import json


class BaseModel():
    """Defines all common attr./methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for key in kwargs.copy():
                if key == "__class__":
                    kwargs.pop("__class__")
                if key == "created_at":
                    self.created_at = datetime.\
                        strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.\
                        strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def __str__(self):
        """returns an unofficial str rep' of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        return object_dict

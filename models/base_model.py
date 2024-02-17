#!/usr/bin/python3
import uuid
from datetime import datetime
import json


class BaseModel():
    """Defines all common attr./methods for other classes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def __str__(self):
        """returns an unofficial str rep' of an instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = type(self).__name__
        return object_dict

#!/usr/bin/python3
import uuid
from datetime import datetime
import json


class BaseModel():
    """Defines all common attr./methods for other classes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat
        self.updated_at = datetime.now().isoformat

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now().isoformat

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        return self.__dict__

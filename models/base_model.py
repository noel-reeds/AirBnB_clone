#!/usr/bin/python3
import uuid
import datetime
import json


class BaseModel():
    """Defines all common attr./methods for other classes"""
    id = str(uuid.uuid4())
    created_at = isoformat(datetime.now())
    updated_at =

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        pass

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        return self.__dict__

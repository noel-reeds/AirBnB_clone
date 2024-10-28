#!/usr/bin/python3
import uuid
from datetime import datetime as dt


class BaseModel:
    """Defines all common attr./methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            if "__class__" in kwargs.keys():
                del kwargs["__class__"]
            if "created_at" in kwargs.keys():
                kwargs["created_at"] = dt.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs.keys():
                kwargs["updated_at"] = dt.fromisoformat(kwargs["updated_at"])
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            # storage.new(self)

    def save(self):
        """ updates attr 'updated_at' with the current datetime"""
        self.updated_at = dt.now()
        # storage.save()

    def __str__(self):
        """returns an unofficial str rep' of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Returns a key-value pair of the instance"""
        attrs = self.__dict__
        attrs['created_at'] = attrs['created_at'].isoformat()
        attrs['updated_at'] = attrs['updated_at'].isoformat()
        attrs['__class__'] = self.__class__.__name__
        return attrs

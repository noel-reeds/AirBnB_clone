#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attr./methods for other classes"""
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            if "__class__" in kwargs.keys():
                del kwargs["__class__"]
            if "created_at" in kwargs.keys():
                kwargs["created_at"] = datetime.\
                    fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs.keys():
                kwargs["updated_at"] = datetime.\
                    fromisoformat(kwargs["updated_at"])
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ updates attr 'updated_at' with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """returns an unofficial str rep' of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

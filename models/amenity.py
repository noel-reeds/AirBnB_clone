#!/usr/bin/python3
"""More classes"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """instantiates an amenity model"""
        super().__init__(*args, **kwargs)

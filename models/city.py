#!/usr/bin/python3
"""city module"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """instantiates a city model"""
        super().__init__(*args, **kwargs)

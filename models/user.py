#!/usr/bin/env python3
"""Models to create a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """instantiates a user model"""
        super().__init__(*args, **kwargs)

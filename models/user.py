#!/usr/bin/env python3
"""Models to create a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/env python3
"""User Creation Model"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

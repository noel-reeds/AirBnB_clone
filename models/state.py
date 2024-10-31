#!/usr/bin/python3
"""models on states"""
from models.base_model import BaseModel


class State(BaseModel):
    """Structure of State model"""
    name = ""

    def __init__(self, *args, **kwargs):
        """instantiates state model"""
        super().__init__(*args, **kwargs)

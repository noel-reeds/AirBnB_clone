#!/usr/bin/python3
"""More classes"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """dunder init method"""
        super().__init__(*args, **kwargs)

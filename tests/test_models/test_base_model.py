#!/usr/bin/python3
"""Tests 'Base Model' module"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class TestBaseModel(unittest.TestCase):
    "Tests case for the base model module"""
    def test_isinstance(self):
        """Tests for isinstance"""
        base = BaseModel()
        amenity = Amenity()
        city = City()
        place = Place()
        state = State()
        review = Review()
        user = User()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(city, City)
        self.assertIsInstance(place, Place)
        self.assertIsInstance(state, State)
        self.assertIsInstance(review, Review)
        self.assertIsInstance(user, User)

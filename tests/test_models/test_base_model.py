#!/usr/bin/python3
"""Tests 'Base Model' module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.user import User


class TestBaseModel(unittest.TestCase):
    "Tests case for the base model module"""
    def test_isinstance(self):
        """Tests for isinstance"""
        base = BaseModel()
        user = User()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(user, User)

    def test_attrs(self):
        """Tests for attrs"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIn('id', base.__dict__.keys())
        self.assertIn('created_at', base.__dict__.keys())
        self.assertIn('updated_at', base.__dict__.keys())

    def test_methods(self):
        base = BaseModel()
        res = base.save()
        self.assertIsInstance(base.updated_at, datetime)

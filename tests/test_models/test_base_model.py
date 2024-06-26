#!/usr/bin/python3
"""Tests 'Base Model' module"""
from unittest.mock import patch
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

    def test_save(self):
        base = BaseModel()
        base.save()
        self.assertIsInstance(base.__dict__['updated_at'], datetime)

    def test_str(self):
        """Tests str method"""
        base = BaseModel()
        res = "[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579)"
        req = base.__str__()
        self.assertNotEqual(req, res)

    def test_attrs_types(self):
        """Tests the data types of attrs"""
        base = BaseModel()
        self.assertIsInstance(base.__dict__['id'], str)
        self.assertIsInstance(base.__dict__['updated_at'], datetime)
        self.assertIsInstance(base.__dict__['created_at'], datetime)

    def test_to_dict(self):
        """Tests to_dict method"""
        base = BaseModel()
        returned = base.to_dict()
        self.assertIsInstance(returned, dict)

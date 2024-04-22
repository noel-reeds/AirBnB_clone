#!/usr/bin/python3
"""Tests 'Base Model' module"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    "Tests case for the base model module"""
    def test_attrs(self):
        """Tests existence of instance attrs"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

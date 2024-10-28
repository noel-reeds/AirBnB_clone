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
        attrs = base.__dict__
        self.assertIsInstance(attrs['updated_at'], datetime)
        self.assertNotEqual(attrs['updated_at'], attrs['created_at'])
        self.assertIn('updated_at', attrs.keys())
        self.assertIsNotNone(attrs['updated_at'])
        self.assertIn(attrs['updated_at'], attrs.values())
        self.assertIn(attrs['created_at'], attrs.values())
        self.assertIn(attrs['id'], attrs.values())
        self.assertNotIsInstance(attrs['updated_at'], str)
        self.assertNotIsInstance(attrs['updated_at'], int)
        self.assertNotIsInstance(attrs['updated_at'], dict)
        self.assertNotIsInstance(attrs['updated_at'], list)

    def test_str(self):
        """Tests str method"""
        base = BaseModel()
        base_dictionary = base.to_dict()
        class_name = base.__class__.__name__
        base_id = base.id
        base_attrs = base.__dict__
        base_str = base.__str__()
        self.assertEqual(base_str, str(base))
        self.assertIsInstance(base_str, str)
        self.assertTrue(base_str.startswith('[BaseModel]'))
        self.assertTrue(base_str.startswith(f"[{class_name}]"))
        self.assertTrue(f"[{class_name}] ({base_id}) {base_attrs}")
        self.assertEqual(f"[{class_name}] ({base_id}) {base_attrs}", str(base))
        self.assertTrue(base_str.endswith(f"{base_attrs}"))
        self.assertEqual(base_id, base_attrs['id'])
        self.assertIn(base_id, base_attrs.values())
        self.assertIn(class_name, base_attrs.values())
        self.assertEqual(class_name, base_dictionary['__class__'])

    def test_attrs_types(self):
        """Tests the data types of attrs"""
        base = BaseModel()
        self.assertIsInstance(base.__dict__['id'], str)
        self.assertIsInstance(base.__dict__['updated_at'], datetime)
        self.assertIsInstance(base.__dict__['created_at'], datetime)

    def test_to_dict(self):
        """Tests to_dict method"""
        base = BaseModel()
        attrs = base.__dict__
        returned = base.to_dict()
        self.assertIsInstance(returned, dict)
        self.assertIn('updated_at', attrs.keys())
        self.assertIn('created_at', attrs.keys())
        self.assertIn('__class__', attrs.keys())
        self.assertIsInstance(attrs['created_at'], str)
        self.assertIsInstance(attrs['updated_at'], str)
        self.assertIn(attrs['updated_at'], attrs.values())
        self.assertIn(attrs['created_at'], attrs.values())

if __name__ == "__main__":
    unittest.main()

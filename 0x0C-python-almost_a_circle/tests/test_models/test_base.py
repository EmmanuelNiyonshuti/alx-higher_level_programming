#!/usr/bin/python3
"""test for base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
class TestBase(unittest.TestCase):
    """Tests Base class"""

    def test__nb_objects_increment(self):
        """Test __nb_objects increment"""
        Base._Base__nb_objects = 0 
        b1 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)
        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)    


    def test_id_None(self):
        self.assertEqual(type(Base()), Base)
        self.assertEqual(Base().id, 5)
        self.assertEqual(Base(None).id, 6)

    def test_valid_id(self):
        self.assertEqual(Base(19).id, 19)
        self.assertEqual(Base(1000).id, 1000)
        self.assertEqual(Base(-78).id, -78)
        self.assertEqual(Base(5.4).id, 5.4)
    def test_to_json_string_with_list(self):
        """Test case with a list of dictionaries"""
        list_dictionaries = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        expected_json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(Base.to_json_string(list_dictionaries), expected_json_string)

    def test_to_json_string_with_empty_list(self):
        """Test case with an empty list"""
        list_dictionaries = []
        self.assertEqual(Base.to_json_string(list_dictionaries), "[]")

    def test_to_json_string_with_none(self):
        """Test case with None"""
        self.assertEqual(Base.to_json_string(None), "[]")
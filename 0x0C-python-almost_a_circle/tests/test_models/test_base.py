#!/usr/bin/python3
"""test for base class"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests Base class"""

    def test_id_None(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        self.assertEqual(type(Base()), Base)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(None).id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_valid_id(self):
        self.assertEqual(Base(19).id, 19)
        self.assertEqual(Base(1000).id, 1000)
        self.assertEqual(Base(-78).id, -78)
        self.assertEqual(Base(5.4).id, 5.4)
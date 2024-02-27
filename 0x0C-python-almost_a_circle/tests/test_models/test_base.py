#!/usr/bin/python3
"""test for base class"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_None(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        r1 = Base()
        r3 = Base(None)
        self.assertEqual(type(r1), Base)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r3.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_id(self):
        r1 = Base(15)
        r2 = Base(1000)
        r3 = Base(0)
        r4 = Base(-89)
        r5 = Base(3.45)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r2.id, 1000)
        self.assertEqual(r3.id, 0)
        self.assertEqual(r4.id, -89)
        self.assertEqual(r5.id, 3.45)
    def test_id_not_int(self):
        r1 = Base("str")
        self.assertEqual(r1.id, 'str')
        r1 = Base([])
        self.assertEqual(r1.id, [])
        r1 = Base([1, 3])
        self.assertEqual(r1.id, [1, 3])
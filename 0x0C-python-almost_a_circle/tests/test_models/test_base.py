#!/usr/bin/python3
"""
This module comprises a class that tests base class.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test base class attributes and methods"""

    def test_id(self):
        """Tests the id instance attribute"""
        base1 = Base()
        base2 = Base(15)
        base3 = Base()
        base4 = Base(12)
        base5 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 15)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, 12)
        self.assertEqual(base5.id, 3)

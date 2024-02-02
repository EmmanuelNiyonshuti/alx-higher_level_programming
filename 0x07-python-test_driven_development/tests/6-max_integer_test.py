import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInt(unittest.TestCase):

    def test_int(self):
        self.AssertEqual(max_integer([1, 2, 3, 4]), 4)
        self.AssertEqual(max_integer([1, 3, 4, 2]), 4)

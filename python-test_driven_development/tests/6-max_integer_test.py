#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test if the max integer is correct

    Args:
        unittest (TestResult): case test of max integer
    """

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_posint_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_int_list(self):
        self.assertEqual(max_integer([56000]), 56000)
        self.assertEqual(max_integer([-56]), -56)

    def test_maxint_first(self):
        self.assertEqual(max_integer([56000, 2, 3, 4]), 56000)

    def test_include_negint(self):
        self.assertEqual(max_integer([-56, -105, -108, -59]), -56)
        self.assertEqual(max_integer([-56, 2, 12, -3, -4]), 12)

    def test_include_float(self):
        self.assertEqual(max_integer([1.5, -2, 3.5, -4.5]), 3.5)
        self.assertEqual(max_integer([-56.5]), -56.5)
        self.assertEqual(max_integer([56.5]), 56.5)
        self.assertEqual(max_integer([-56.5, 2.5, -12.5, 3.5, -4.5]), 3.5)

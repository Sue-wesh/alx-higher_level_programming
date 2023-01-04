#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """define unittest for function max_integer"""

    def test_ordered_list(self):
        a_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(a_list), 4)

    def test_unordered_list(self):
        a_list = [1, 3, 4, 2]
        self.assertEqual(max_integer(a_list), 4)

    def test_empty_list(self):
        a_list = []
        self.assertEqual(max_integer(a_list), None)

    def test_max_value(self):
        a_list = [9, 15, 4, 7]
        self.assertEqual(max_integer(a_list), 15)

if __name__ == '__main__':
    unittest.main()

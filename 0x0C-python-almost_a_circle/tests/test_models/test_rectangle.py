#!/usr/bin/python3

"""defines unit tests for rectangle.py"""

import os
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """test for the Rectangle class."""

    def test_id(self):
        """test of rectangle ids"""
        Base.__Base__nb_objects = 0

        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1.id, rect2.id - 1)

        rect3 = Rectangle(4, 3, 9)
        self.assertEqual(rect3.id, rect2.id + 1)

        rect4 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect4.id, rect3.id + 1)

        rect5 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect5.id, 12)

    def test_type_exceptions(self):
        """test when there is a type error."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_exceptions(self):
        """test when there is a value error"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

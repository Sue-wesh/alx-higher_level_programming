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
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1.id, rect2.id - 1)

        rect3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect3.id, 12)

#!/usr/bin/python3

"""defines unittest for Rectangle class"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_Instatiate(unittest.TestCase):
    """different test cases"""
    def test_inheritannce(self):
        self.assertEqual(Rectangle(3, 4, 1, 2, 5).id, Base(5).id)
    
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_str(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2, 3, 4)

    def test_width_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4)

    def test_height_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2", 3, 4)

    def test_hei_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4)

    def test_x_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3", 4)

    def test_y_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_area(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 2
        r.height = 10
        self.assertEqual(20, r.area())

class TestRectangle_stdout(unittest.TestCase):
    """unittest for testing display"""

    def printToStdout(rect, meth):
        """returns text printed to stdout
        Args:
        rect (Rectangle)
        meth (method)
        """

        std_out = io.StringIO()
        sys.stdout = std_out
        if meth == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__

        return std_out

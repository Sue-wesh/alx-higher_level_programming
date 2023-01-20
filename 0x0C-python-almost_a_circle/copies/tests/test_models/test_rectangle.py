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

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two(self):
        r1 = Rectangle(5, 7)
        r2 = Rectangle(10, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_five(self):
        self.assertEqual(3, Rectangle(2, 4, 7, 9, 3).id)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
    
    def test_width_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 9, 0, 0, 1).__width)

    def test_height_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 9, 0, 0, 1).__height)

    def test_x_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 9, 0, 0, 1).__x)

    def test_y_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 9, 0, 0, 1).__y)

    def test_width_get(self):
        self.assertEqual(2, Rectangle(2, 3, 7, 9, 4).width)

    def test_width_set(self):
        r = Rectangle(2, 3, 7, 9, 4)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_get(self):
        self.assertEqual(3, Rectangle(2, 3, 7, 9, 4).height)

    def test_height_set(self):
        r = Rectangle(2, 3, 7, 9, 4)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_get(self):
        self.assertEqual(7, Rectangle(2, 3, 7, 9, 4).x)
    
    def test_x_set(self):
        r = Rectangle(2, 3, 7, 9, 4)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_get(self):
        self.assertEqual(9, Rectangle(2, 3, 7, 9, 4).y)

    def test_y_set(self):
        r = Rectangle(2, 3, 7, 9, 4)
        r.y = 10
        self.assertEqual(10, r.y)



class Test_width(unittest.TestCase):
    """test the width attribute in Rectangle class"""

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
    
    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.9, 6)

    def test_neg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)



class Test_height(unittest.TestCase):
    """test height attribute in Rectangle class"""
    
    def test_ht_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_ht_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_ht_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 3.6)

    def test_ht_neg(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)



class Test_x(unittest.TestCase):
    """test x attribute in Rectangle class"""

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3", 4)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 6.1, 7)

    def test_x_neg(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, 4)



class Test_y(unittest.TestCase):
    """test y attribute in Rectangle class"""

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 4.5)

    def test_y_neg(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


class Test_area(unittest.TestCase):
    """test area method of Rectangle class"""

    def test_area(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(2, r.area())



class TestRectangle_stdout(unittest.TestCase):
    """unittest for testing display and str methods"""
    
    @staticmethod
    def printToStdout(rect, meth):
        """returns text printed to stdout
        Args:
        rect (Rectangle)
        meth (method)
        """

        stdOut = io.StringIO()
        sys.stdout = stdOut
        if meth == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return stdOut

    def test_str_WidthHeight(self):
        r = Rectangle(4, 6)
        stdOut = TestRectangle_stdout.printToStdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, stdOut.getvalue())

    def test_str_WidthHeight_X(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_WidthHeight_X_Y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_WidthHeight_X_Y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_one(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display(self):
        r = Rectangle(2, 3, 0, 0, 0)
        stdOut = TestRectangle_stdout.printToStdout(r, "display")
        self.assertEqual("##\n##\n##\n", stdOut.getvalue())

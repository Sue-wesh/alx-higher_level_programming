#!/usr/bin/python3

"""defines unit tests for base.py."""

import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """test instatiation of the Base class."""

    def test_baseid(self):
        """
        test base() for assigning id automatically
        """
        b1 = Base()
        b2 = Base()
        self.assertTrue(b1.id, 1)
        self.assertEqual(b1.id, b2.id - 1)

        b3 = Base(85)
        self.assertTrue(b3.id, 85)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
    
    def test_with_id(self):
        self.assertEqual(12, Base(12).id)
    
    def test_baseOneThree(self):
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("happy", Base("happy").id)

    def test_float_id(self):
        self.assertEqual(4.7, Base(4.7).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        """test base to json string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        dict1 = {'id': 2, 'width': 3, 'height': 4, 'x':2, 'y': 4}
        dict2 = {'id': 6, 'width': 6, 'height': 8, 'x':4, 'y': 8}
        jsonize = Base.to_json_string([dict1, dict2])
        dict3 = json.loads(jsonize)
        self.assertEqual(dict3, [dict1, dict2])

    def test_from_json_string(self):
        """test base from json string"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_rectangle(self):
        """test of rectangle exists"""
        rect1 = Rectangle(10, 2)
        self.assertEqual(rect1.id, 7)

        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1.id, rect2.id - 1)

        rect3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect3.id, 12)

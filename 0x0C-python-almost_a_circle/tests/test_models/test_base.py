#!/usr/bin/python3

"""defines unit tests for base.py."""

import os
import unittest
from models.base import Base


class TestBaseInstatiation(unittest.TestCase):
    """test instatiation of the Base class."""

    def test_baseid(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_baseOneTwo(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

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

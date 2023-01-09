#!/usr/bin/python3

"""defines a class BaseGeometry."""

class BaseGeometry:
    """represents class BaseGeometry"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    """public instance method integer_validator"""

    def integer_validator(self, name, value):
        """method validates value.
        if value is not an integer raise a TypeError Exception
        raise a ValueError exception if its less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

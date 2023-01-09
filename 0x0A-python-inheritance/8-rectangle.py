#!/usr/bin/python3

"""defines a class Rectangle. it inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """represents class Rectangle"""

    def __init__(self, width, height):
        """instantiated with width and height"""
        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

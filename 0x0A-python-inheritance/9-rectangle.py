#!/usr/bin/python3

"""defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """represents class Rectangle"""

    def __init__(self, width, height):
        """instantiated with private attributes width and height"""
        
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """for print() and str() representations"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

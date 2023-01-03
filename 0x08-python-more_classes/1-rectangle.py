#!/usr/bin/python3

"""defines a Rectangle class based on 0-rectangle.py"""

class Rectangle:

    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    """getter for width"""

    @property
    def width(self):
        return (self.__width)
    
    """setter for width"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
    
    """getter for height"""

    @property
    def height(self):
        return (self.__height)
    
    """setter for height"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

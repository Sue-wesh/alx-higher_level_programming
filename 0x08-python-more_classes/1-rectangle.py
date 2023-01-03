#!/usr/bin/python3

"""defines a Rectangle class based on 0-rectangle.py"""

class Rectangle:

    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle with arguments:
        width initialized at 0
        height initialized at 0
        """

        self.width = width
        self.height = height
    
    @property
    def width(self):
        """get width of rectangle"""
        return (self.__width)
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
    
    @property
    def height(self):
        """get height of the rectangle"""
        return (self.__height)
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

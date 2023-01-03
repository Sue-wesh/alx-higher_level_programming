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

    def area(self):
        """find the area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """return printable representation of a rectangle

        represent rectangle with # character
        """

        if self.__width == 0 or self.__height == 0:
            return("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return string representation of rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) +")"
        return (rect)

    def __del__(self):
        """print a message for every instance of rectangle deleted"""
        print("Bye rectangle...")

#!/usr/bin/python3

"""define class Square"""
class Square:
    """methos __init__ to initialize"""

    def __init__(self, size=0):
        """object calls itself using self"""

        self.__size = size

    """getter method"""
    @property
    def size(self):
        return (self.__size)

    """setter method"""
    @size.setter
    def size(self, size):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    """instance method to get area"""
    def area(self):
        return(self.__size * self.__size)

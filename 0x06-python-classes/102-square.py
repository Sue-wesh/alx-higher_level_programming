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
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    """instance method to get area"""
    def area(self):
        return(self.__size * self.__size)

    def __eq__(self, other):
        """ for comparator '==' """
        return self.area() == other.area()

    def __ne__(self, other):
        """ for comparator '!=' """
        return self.area() != other.area()

    def __gt__(self, other):
        """ for comparator '>' """
        return self.area() > other.area()

    def __ge__(self, other):
        """ for comparator '>=' """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ for comparator '<' """
        return self.area() < other.area()

    def __le__(self, other):
        """ for comparator '<=' """
        return self.area() <= other.area()

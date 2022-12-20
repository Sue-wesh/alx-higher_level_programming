#!/usr/bin/python3

"""define a class Square"""

class Square:
    """create a method to initialize"""
    
    def __init__(self, size=0):
        """typeerror for if its not an integer"""
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """raise valueerror is its below 0"""

        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

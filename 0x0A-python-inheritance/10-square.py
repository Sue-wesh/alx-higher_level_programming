#!/usr/bin/python3

"""defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """represents a class Square"""

    def __init__(self, size):
        """instantiate Square with private attribute size"""
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3

"""defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """represents class Square"""

    def __init__(self, size):
        """instates with private attr size"""
        
        self.integer_validator
        super().__init__(size, size)
        self.__size = size

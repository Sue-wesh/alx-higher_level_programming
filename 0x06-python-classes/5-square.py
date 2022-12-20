#!/usr/bin/python3

"""define a class square """

class Square:

    """inintialize using method __init__"""

    def __init__(self, size=0):

        """call the object using self """

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

    """instance method area to get area"""

    def area(self):
        return (self.__size * self.__size)

    """intance method my_print that prints in stdout square with
    character #"""

    def my_print(self):
        """print the square with # character #"""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if (self.__size == 0):
            print("")

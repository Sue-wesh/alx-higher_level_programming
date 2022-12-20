#!/usr/bin/python3

"""define a class Square"""

class Square:

    """method __init__ for initializing"""

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

    """retrieve size"""

    @property
    def size(self):
        return (self.__size)

    """set it"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value
    """retrieve position"""

    @property
    def position(self):
        return (self.__position)

    """set position"""

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        size.__position = value

    """instance method area"""

    def area(self):
        return (self.__size * self.__size)

    """instance method my_print"""

    def my_print(self):
        if (self.__size == 0):
            print("")
            return
            
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i  in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")

#!/usr/bin/python3

"""defines a square with character #"""

def print_square(size):
    """raises a TypeError exception if:
        -- size is not an integer
        -- size is a float and is less than 0
        """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    """raises a ValueError is size is < 0"""

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")

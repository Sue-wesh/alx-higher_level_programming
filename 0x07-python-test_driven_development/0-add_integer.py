#!/usr/bin/python3

"""integer addition function."""


def add_integer(a, b=98):
    """
    This function adds two integers returns the sum of the two integers.

    if a or b is a float its first casted to integer before adding
    """
    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

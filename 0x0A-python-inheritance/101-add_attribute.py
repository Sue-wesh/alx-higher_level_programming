#!/usr/bin/python3

"""function adds new attribute to an object"""

def add_attribute(obj, att, value):
    """
    represents function that adds new attribute to an object
    Raises TypeError if the attribute cant be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

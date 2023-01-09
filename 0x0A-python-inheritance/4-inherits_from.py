#!/usr/bin/python3

"""defines a function that returns True if the object is instance of class that inherited"""

def inherits_from(obj, a_class):
    """
    returns True if:
    ... he object is an instance of a class that inherited 
    ... (directly or indirectly) from the specified class
    otherwise returns False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

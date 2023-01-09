#!/usr/bin/python3

"""define a function that returns True for a certain instance of the object."""

def is_same_class(obj, a_class):
    """if function to check if the obj of the specified instance
    return True if 
    ... the object is an instance of, 
    ... or if the object is an instance of a class that inherited from, 
    ... the specified class ; 

    ... otherwise False
    """
    if type(obj) == a_class:
        return True
    return False

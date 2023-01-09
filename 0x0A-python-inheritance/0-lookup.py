#/usr/bin/python3

"""
defines lookup function that returns a lits of attributes and methods of an object
"""

def lookup(obj):
    """
    return a list of attributes and methods of an object.
    """
    return (dir(obj))

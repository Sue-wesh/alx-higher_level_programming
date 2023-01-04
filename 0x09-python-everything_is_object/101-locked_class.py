#!/usr/bin/python3

"""define a LockedClass"""

class LockedClass:
    """
    prevent the user from dynamically creating new instance attributes
    except the new instance attribute first_name
    """
    __slots__ = ["first_name"]

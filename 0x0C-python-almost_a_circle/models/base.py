#!/usr/bin/python3

"""defines the Base class"""

class Base:
    """
    represents the base of all other classes in this project.
    Goal---
    To manage id attribute in all future classes and
    and avoid duplicating the same code
    
    private class attribute __nb_objects = 0
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize the base class.
        if id is not None, assign the public instance attribute id with this argument value 
        otherwise increment __nb_objects and assign the new value to the public instance attribute id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


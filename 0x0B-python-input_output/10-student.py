#!/usr/bin/python3

"""defines a class Student"""

class Student:
    """represents class Student"""

    def __init__(self, first_name, last_name, age):
        """instatiate with students first and last names and their age"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a student instance
        if attrs is a list of strings
        ,,, only attribute names contained in this list must be retrieved
        otherwise, all attributes must be retrieved"""

        if (type(attrs) == list

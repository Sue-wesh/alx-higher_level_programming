#!/usr/bin/python3

"""defines a class Student."""

class Student:
    """represents class Student"""

    def __init__(self, first_name, last_name, age):
        """instatiate with student first and last names and their age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict representation of Student"""

        return (self.__dict__)

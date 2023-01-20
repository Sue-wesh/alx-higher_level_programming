#!/usr/bin/python3

"""defines the Base class"""
import json


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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """the JSON string representation of list_dictionaries
        list_dictionaries is a list of dictionaries
        If list_dictionaries is None or empty, return the string: "[]"
        else
        return the JSON string representation of list_dictionaries.
        """
        
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base
        eg list of Rectangle or Square instances
        If list_objs is None, save an empty list
        filename must be: <Class name>.json
        use the static method to_json_string
        overwrite the file if it already exists
        """
        filename = cls.__name__ + ",json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [x.to_dictionary() for x in list_obj]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string representation json_string.
        json_string is a string representing a list of dictionaries
        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

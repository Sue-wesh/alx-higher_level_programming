#!/usr/bin/python3

"""function creates an Object from a JSON file"""
import json

def load_from_json_file(filename):
    """create an Object
    normally we would have json.load(my_obj), but from a JSON file would
    give a diff approach
    """

    with open(filename) as f6:
        return (json.load(f6))

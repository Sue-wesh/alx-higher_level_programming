#!/usr/bin/python3

"""function that writes an Object to a text file using JSON representation"""
import json

def save_to_json_file(my_obj, filename):
    """writing an object using JSON"""

    with open(filename, "w") as f5:
        json.dump(my_obj, f5)

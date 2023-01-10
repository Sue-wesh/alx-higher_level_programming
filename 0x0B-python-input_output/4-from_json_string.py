#!/usr/bin/python3

"""function that returns an object (Python data structure)
thats represented by a JSON string"""
import json

def from_json_string(my_str):
    """decode JSON and return the object thats represented by JSON string"""

    return (json.loads(my_str))

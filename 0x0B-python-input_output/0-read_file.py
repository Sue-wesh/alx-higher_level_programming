#!/usr/bin/python3

"""function reads a text in encoding algorithm utf-8"""

def read_file(filename=""):
    """open the file and read the text in it"""
    
    with open(filename, encoding='utf-8') as file_one:
        print(file_one.read())

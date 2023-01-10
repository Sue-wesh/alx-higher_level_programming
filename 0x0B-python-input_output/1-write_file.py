#!/usr/bin/python3

"""function writes a string to a text file."""

def write_file(filename="", text=""):
    """open a file and write some text inside it."""
    
    with open(filename, mode="w", encoding="utf-8") as f1:
        return f1.write(text)

#!/usr/bin/python3

"""function appends a string at the end of a text file
returns no of characters added"""

def append_write(filename="", text=""):
    """open the file filename and append text"""

    with open(filename, mode="a", encoding="utf-8") as f2:
        return (f2.write(text))

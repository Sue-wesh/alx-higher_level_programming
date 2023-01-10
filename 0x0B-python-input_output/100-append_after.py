#!/usr/bin/python3

"""function that inserts a line of text to a file"""
def append_after(filename="", search_string="", new_string=""):
    """append after a certain string"""
    
    text = ""
    with open(filename) as f13:
        for line in f13:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)

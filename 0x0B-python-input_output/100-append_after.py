#!/usr/bin/python3
"""Module that defines a text file insertion func"""


def append_after(filename="", search_string="", new_string=""):
    """Add text following every line that contains a specific string within a file.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

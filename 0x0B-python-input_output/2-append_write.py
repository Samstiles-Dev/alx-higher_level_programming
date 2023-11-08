#!/usr/bin/python3
"""Function that appends a file"""


def append_write(filename="", text=""):
    """function that opens and append a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

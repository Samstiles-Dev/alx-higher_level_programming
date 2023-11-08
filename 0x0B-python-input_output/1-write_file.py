#!/usr/bin/python3
"""Function that writes into a file"""


def write_file(filename="", text=""):
    """Function that writes into file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

#!/usr/bin/python3
"""
   Mod/Func that writes into a file, a json obj
"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes json into a file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)

#!/usr/bin/python3
"""
   Mod that returns a python struct,
   from a JSON string
"""


import json


def from_json_string(my_str):
    """function that returns python structure"""
    return json.loads(my_str)

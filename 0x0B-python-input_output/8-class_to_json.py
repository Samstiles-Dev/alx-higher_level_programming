#!/usr/bin/python3
"""Module that defines a Python class-to-JSON func"""


def class_to_json(obj):
    """Returns the dict representation of a simple data structure"""
    return obj.__dict__

#!/usr/bin/python3
"""
   Mod that checks if an obj is an instance,
   or inherited from a sub-class
"""


def is_kind_of_class(obj, a_class):
    """checks for obj instance compared to a class"""
    return (isinstance(obj, a_class))

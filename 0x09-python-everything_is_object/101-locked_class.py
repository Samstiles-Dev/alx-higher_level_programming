#!/usr/bin/python3
"""This class prevents user from creating new instance att"""


class LockedClass:
    """
    Only allows an attribute called first_name
    """

    __slots__ = ["first_name"]

#!/usr/bin/python3
"""Mod that inherits a list and prints the element"""


class MyList(list):
    """class that inherits list and prints its attribute"""
    def print_sorted(self):
        """Method that prints sorted list"""
        print(sorted(self))

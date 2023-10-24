#!/usr/bin/python3
"""does exactly the same as the following Python bytecode:"""
import math


class MagicClass:
    """the Initialization of the MagicClass."""
    def __init__(self, radius=0):
        """magic class constructor"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """calculates the area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """calculates the circumference."""
        return 2 * math.pi * self._MagicClass__radius

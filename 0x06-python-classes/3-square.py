#!/usr/bin/python3
"""Module that defines a square"""


class Square:
    """creates a private instance attribute"""

    def __init__(self, size=0):
        """stat Initializing this square class
        Args:
            size: this represents the size of the square defined
        Raises:
            TypeError: i.e if size is not integer
            ValueError: i.e if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of square"""
        return self.__size ** 2

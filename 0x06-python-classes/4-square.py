#!/usr/bin/python3
"""Module that defines a square"""


class Square:
    """this Defines a class that creates squares"""
    def __init__(self, size=0):
        """stat Initializing this square class
        Args:
            size: this represents the size of the square defined
        Raises:
            TypeError: i.e if size is not integer
            ValueError: i.e if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """ this function returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """ this function sets the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """this function defines the area"""
        return self.__size ** 2

#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Init the rectangle class
        Args:
            width: reps the width of the rectangle
            height: reps the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

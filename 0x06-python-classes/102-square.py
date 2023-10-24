#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """this defines the square class"""

    def __init__(self, size=0):
        """this Create a Square
        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """"The propery of size as the lenght of a side of Square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """this Gets the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

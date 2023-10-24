#!/usr/bin/python3
"""Module that defines a square"""


class Square:
    """this function Creates a square"""
    def __init__(self, size=0, position=(0, 0)):
        """this function creates attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """this function returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """this function sets size and value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """this function returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """this function sets position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """this function sets area"""
        return self.size ** 2

    def my_print(self):
        """this function prints attributes"""
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

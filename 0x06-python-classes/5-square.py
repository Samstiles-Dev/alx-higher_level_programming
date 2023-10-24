#!/usr/bin/python3
"""Module that defines a square"""


class Square:
    """this function defines a sqaure class"""
    def __init__(self, size=0):
        """initialising the size variable"""
        self.size = size

    @property
    def size(self):
        """this function returns private attibute"""
        return self.__size

    @size.setter
    def size(self, value):
        """this function checks the value passed"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """this function sets the area"""
        return self.__size ** 2

    def my_print(self):
        """this function prints the size"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

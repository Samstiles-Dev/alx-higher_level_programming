#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this class repres a rectangle"""
    number_of_instances = 0
    _print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init this rectangle class
        Args:
            width: repres the width of the rectangle
            height: repres the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width attribute"""
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

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        _rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    _rectangle += str(self._print_symbol)
                except Exception:
                    _rectangle += type(self)._print_symbol
            if column < self.__height - 1:
                _rectangle += "\n"
        return (_rectangle)

    def __repr__(self):
        """returns a str repres of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a msg for every obj that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

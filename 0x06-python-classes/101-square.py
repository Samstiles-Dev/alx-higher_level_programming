#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """this defines a class Square."""

    def __str__(self):
        """print the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """this initialize the square with this
        Args:
            size: a side of square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """this is the property of the length of a side of square
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """this is set the size of square
        Args:
            value: the size of the square
        Raises:
                TypeError: if value is not int
                ValueError: if valie < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """the property of the position of square
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """this set the position
        Args:
            value: where to set the position
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: the position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ the area of square
        Returns:
            area = size * size
        """
        return self.__size * self.__size

    def pos_print(self):
        """this returns the printed square with position"""
        _pos = ""
        if not self.size:
            return "\n"
        for v in range(self.position[1]):
            _pos += "\n"
        for v in range(self.size):
            for h in range(self.position[0]):
                _pos += " "
            for n in range(self.size):
                _pos += "#"
            _pos += "\n"
        return _pos

    def my_print(self):
        """this prints the square"""
        print(self.pos_print(), end="")

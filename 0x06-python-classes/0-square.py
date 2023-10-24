#!/usr/bin/python3
"""Square module - Defines a simple Square class."""

class Square:
    """
    Square class represents a simple square.

    Attributes:
        side (int): The length of each side of the square.
    """

    def __init__(self, side=0):
        """
        Initializes a new Square with a specified side length.

        Args:
            side (int): The length of each side of the square.

        """
        self.side = side

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.side ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.side

if __name__ == "__main__":
    my_square = Square(5)
    print(f"{my_square.side}")
    print(f"Area: {my_square.area()}")
    print(f"Perimeter: {my_square.perimeter()}")


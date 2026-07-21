#!/usr/bin/python3
"""Defines a Square class that supports comparison operators."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int/float): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares do not have the same area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if this square's area is greater than another's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square's area is greater than or equal."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if this square's area is less than another's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square's area is less than or equal."""
        return self.area() <= other.area()

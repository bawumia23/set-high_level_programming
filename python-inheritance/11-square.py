#!/usr/bin/python3
"""Module that defines a Square class extending Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a special case of Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square's sides, must be positive.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square.

        Returns:
            str: formatted as "[Square] <width>/<height>".
        """
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)

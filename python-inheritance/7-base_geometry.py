#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area and validation."""


class BaseGeometry:
    """Base class for all geometry shapes."""

    def area(self):
        """Compute the area of the shape.

        Raises:
            Exception: always, since this method must be overridden
                by a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): the name of the attribute being validated.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer (bool does not count
                as a valid integer here).
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

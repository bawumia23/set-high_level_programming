#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Base class for all geometry shapes."""

    def area(self):
        """Compute the area of the shape.

        Raises:
            Exception: always, since this method must be overridden
                by a subclass.
        """
        raise Exception("area() is not implemented")

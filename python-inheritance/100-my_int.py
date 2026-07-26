#!/usr/bin/python3
"""Module that defines a MyInt class extending int with flipped
comparisons."""


class MyInt(int):
    """An int whose == and != operators are inverted."""

    def __eq__(self, other):
        """Return the inverse of the normal equality check."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return the inverse of the normal inequality check."""
        return int(self) == int(other)

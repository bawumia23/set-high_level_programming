#!/usr/bin/python3
"""Module that defines a MyList class extending the built-in list."""


class MyList(list):
    """A list that can print its contents in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        The list itself is left unmodified.
        """
        print(sorted(self))

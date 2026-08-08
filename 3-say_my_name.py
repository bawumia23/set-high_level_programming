#!/usr/bin/python3
"""Module for printing a full name.

This module provides a function that prints a formatted
full name from first and last name strings.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

    Args:
        first_name: The first name, must be a string.
        last_name: The last name, must be a string (default is empty).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

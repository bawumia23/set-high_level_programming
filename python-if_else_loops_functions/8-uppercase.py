#!/usr/bin/python3
"""Module for printing a string in uppercase."""


def uppercase(str):
    """Print a string in uppercase, followed by a newline.

    Args:
        str: the string to print in uppercase
    """
    print("{}".format("".join(
        chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c for c in str)))

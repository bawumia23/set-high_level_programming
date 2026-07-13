#!/usr/bin/python3
"""Module for removing a character at a given position in a string."""


def remove_char_at(str, n):
    """Return a copy of the string with the character at index n removed.

    Args:
        str: the original string
        n: the index of the character to remove

    Returns:
        A new string with the character at position n removed
    """
    if n < 0:
        return str
    return str[:n] + str[n + 1:]

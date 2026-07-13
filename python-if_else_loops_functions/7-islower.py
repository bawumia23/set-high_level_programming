#!/usr/bin/python3
"""Module for checking lowercase characters."""


def islower(c):
    """Check if a character is lowercase.

    Args:
        c: the character to check

    Returns:
        True if c is lowercase, False otherwise
    """
    return 97 <= ord(c) <= 122

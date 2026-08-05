#!/usr/bin/python3
"""Module to write to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename: The name of the file to write to.
        text: The text to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Module to append text after a specific string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string.

    Args:
        filename: The name of the file.
        search_string: The string to search for in each line.
        new_string: The string to insert after lines containing search_string.
    """
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()

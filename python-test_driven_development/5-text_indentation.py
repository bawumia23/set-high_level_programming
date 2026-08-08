#!/usr/bin/python3
"""Module for text indentation.

This module provides a function that prints text with
two new lines after each '.', '?', and ':' character.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text: The text to print, must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1

    print(result, end="")

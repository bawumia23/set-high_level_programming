#!/usr/bin/python3
"""Module for printing the last digit of a number."""


def print_last_digit(number):
    """Print the last digit of a number and return its value.

    Args:
        number: the number to process

    Returns:
        The last digit of number (always non-negative)
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

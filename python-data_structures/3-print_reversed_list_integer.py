#!/usr/bin/python3
"""Module that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of my_list, one per line, in reverse order.

    Does nothing if my_list is None.
    """
    if my_list is None:
        return
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))

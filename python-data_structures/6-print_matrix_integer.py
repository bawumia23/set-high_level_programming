#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, row by row, space-separated."""
    for row in matrix:
        line = ""
        for i in range(len(row)):
            if i == len(row) - 1:
                line += "{:d}".format(row[i])
            else:
                line += "{:d} ".format(row[i])
        print(line)

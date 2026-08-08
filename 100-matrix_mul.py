#!/usr/bin/python3
"""Module for matrix multiplication.

This module provides a function that multiplies two matrices
with full validation of inputs.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: First matrix, a list of lists of integers or floats.
        m_b: Second matrix, a list of lists of integers or floats.

    Returns:
        list: A new matrix representing the product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains non-numeric elements, or rows are not
                   of the same size.
        ValueError: If m_a or m_b is empty, or if they cannot be
                    multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = 0
            for k in range(len(m_b)):
                elem += m_a[i][k] * m_b[k][j]
            row.append(elem)
        result.append(row)

    return result

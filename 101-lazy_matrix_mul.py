#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy.

This module provides a function that multiplies two matrices
using the numpy module for efficient computation.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: First matrix, a list of lists of integers or floats.
        m_b: Second matrix, a list of lists of integers or floats.

    Returns:
        numpy.ndarray: The product of m_a and m_b.

    Raises:
        ValueError: If matrices cannot be multiplied.
        TypeError: If inputs are not valid for matrix multiplication.
    """
    return np.matmul(m_a, m_b)

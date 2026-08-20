#!/usr/bin/python3
"""Module that finds a peak value in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find and return a peak value from a list of unsorted integers.

    A peak is an element that is not smaller than its neighbors. The
    search uses a binary-search style approach for O(log(n)) time.
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]

    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]

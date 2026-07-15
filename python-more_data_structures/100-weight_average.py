#!/usr/bin/python3
"""Module that computes the weighted average of a list of tuples."""


def weight_average(my_list=[]):
    """Return the weighted average of a list of (score, weight) tuples.

    Args:
        my_list (list): list of tuples (<score>, <weight>).

    Returns:
        float: the weighted average, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_weighted_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)

    return total_weighted_score / total_weight

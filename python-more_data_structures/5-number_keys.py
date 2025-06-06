#!/usr/bin/python3
def number_keys(a_dictionary):
    """Number of keys in a dictionary

    Args:
        a_dictionary (dict): the dictionary

    Returns:
        int: Number of keys
    """
    res = 0
    for i in a_dictionary:
        res += 1
    return res

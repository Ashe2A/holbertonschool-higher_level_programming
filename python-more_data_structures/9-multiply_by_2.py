#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiply a dictionary by 2

    Args:
        a_dictionary (dict): The original dictionary

    Returns:
        dict: The new doubled dictionary
    """
    new_dictionary = {}
    for i in a_dictionary:
        new_dictionary[i] = a_dictionary[i] * 2
    return new_dictionary

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiply by 2 a dictionary.

    Parameters:
        a_dictionary : the dictionary

    Returns:
        New updated dictionary
    """
    new_dictionary = []
    for i in list(a_dictionary):
        new_dictionary[i] = a_dictionary[i] * 2
    return new_dictionary

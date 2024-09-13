#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiply by 2 a dictionary.

    Parameters:
        a_dictionary : the dictionary

    Returns:
        New updated dictionary
    """
    new_dictionary = a_dictionary[:]
    for i in list(new_dictionary):
        new_dictionary[i] *= 2

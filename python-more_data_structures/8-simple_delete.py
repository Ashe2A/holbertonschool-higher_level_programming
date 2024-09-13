#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Updates a dictionary.

    Parameters:
        a_dictionary : the dictionary
        key : key to remove the value of

    Returns:
        Updated dictionary
    """
    del a_dictionary[key]
    return a_dictionary

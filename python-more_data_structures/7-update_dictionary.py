#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary.

    Parameters:
        a_dictionary : the dictionary.
        key : key to create/to update the value of
        value : value to add

    Returns:
        Updated dictionnary
    """
    a_dictionary[key] = value
    return a_dictionary

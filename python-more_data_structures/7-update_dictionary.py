#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''Update a dictionary key/value pairing

    Args:
        a_dictionary (dict): the dictionary
        key (str): the updated or new key
        value (obj): the updated or new value

    Returns:
        dict: the updated dictionary
    '''
    a_dictionary[key] = value
    return a_dictionary

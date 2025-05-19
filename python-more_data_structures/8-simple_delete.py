#!/usr/bin/python3
def simple_delete(a_dictionary, key=''):
    '''Delete a dictionary entry

    Args:
        a_dictionary (dict): The dictionary
        key (str, optional): The key of the entry to delete.
            Defaults to empty string.

    Returns:
        dict: the updated dictionary
    '''
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

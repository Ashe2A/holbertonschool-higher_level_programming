#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list.

    Parameters:
        my_list (list) : the list.
        idx (int) : the element's index in the list
        element (void) : the element to insert

    Returns:
        The modified (or not) list
    """
    if (0 <= idx < len(my_list)):
        my_list[idx] = element
    return my_list

#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a copy of a list.

    Parameters:
        my_list (list) : the list to copy.
        idx (int) : the element's index in the list.
        element (void) : the element to insert in the copy.

    Returns:
        The new list
    """
    new_list = my_list
    if (0 <= idx < len(new_list)):
        new_list[idx] = element
    return new_list

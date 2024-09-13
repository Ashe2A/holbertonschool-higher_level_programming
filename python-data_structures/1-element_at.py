#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list.

    Parameters:
        my_list (list) : the list.
        idx (int) : the element's index in the list

    Returns:
        The element in the list, "None" if error
    """
    if (idx > len(my_list)) or (idx < 0):
        return "None"
    return my_list[idx]

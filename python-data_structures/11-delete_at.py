#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Remove list elements.

    Parameters:
        my_list (list) : item list.
        idx : index of the item to remove

    Returns:
        modified (or not) list
    """
    if (my_list != []) or (0 <= idx < len(my_list)):
        del (my_list[idx])
    return my_list

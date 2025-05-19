#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''Replaces an element in a list

    Args:
        my_list (list): The list
        idx (int): The index of the element
        element (obj): The new element

    Returns:
        The list (modified or not)
    '''
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list

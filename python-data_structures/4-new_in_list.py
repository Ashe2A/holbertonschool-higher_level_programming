#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list copy

    Args:
        my_list (list): The old list
        idx (int): The index of the element
        element (obj): The new element

    Returns:
        The new list
    """
    new_list = []
    for i in my_list:
        new_list.append(i)
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list

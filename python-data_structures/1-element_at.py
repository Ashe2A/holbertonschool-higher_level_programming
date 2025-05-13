#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an elements from a list

    Args:
        my_list (list): The list
        idx (int): The index of the element

    Returns:
        obj: The retrieved element
    """
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None

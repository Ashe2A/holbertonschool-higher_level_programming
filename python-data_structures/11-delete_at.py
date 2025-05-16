#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes an element of a list

    Args:
        my_list (list, optional): The list. Defaults to empty list.
        idx (int, optional): The specified index. Defaults to 0 (first index).

    Returns:
        list: The list minus the deleted element
    """
    if 0 <= idx < len(my_list):
        my_list.remove(idx + 1)
    return my_list

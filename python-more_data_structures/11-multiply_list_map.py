#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Multiply all list elements

    Args:
        my_list (list, optional): The list. Defaults to empty list.
        number (int, optional): The multiplier. Defaults to 0.

    Returns:
        list: The new list
    """
    return list(map(lambda i: i * number, my_list))

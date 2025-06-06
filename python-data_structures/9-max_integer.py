#!/usr/bin/python3
def max_integer(my_list=[]):
    """Largest integer of a list

    Args:
        my_list (list, optional): The list. Defaults to empty list.

    Returns:
        int: The largest integer
    """
    if my_list == []:
        return None
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max

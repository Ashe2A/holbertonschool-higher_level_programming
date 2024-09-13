#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Max integer.

    Parameters:
        my_list (list) : integer list.

    Returns:
        The max of an integer list
    """
    if my_list == []:
        return None
    super_max = my_list[0]
    for i in my_list:
        if i > super_max:
            super_max = i
    return super_max

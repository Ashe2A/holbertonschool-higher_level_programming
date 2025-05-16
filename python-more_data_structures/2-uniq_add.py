#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in the list

    Args:
        my_list (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    unique_list = []
    res = 0
    for i in my_list:
        if i not in unique_list:
            res += i
            unique_list.append(i)
    return res

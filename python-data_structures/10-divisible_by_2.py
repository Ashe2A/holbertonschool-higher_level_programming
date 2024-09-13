#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    My list is divisible by 2.

    Parameters:
        my_list (list) : integer list.

    Returns:
        Bool list of whetever list-corresponding indexes are divisible by 2.
    """
    boolist = []
    for i in my_list:
        if (i % 2) == 0:
            boolist.append(True)
        else:
            boolist.append(False)
    return boolist

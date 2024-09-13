#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all distinct integers from a list (meaning dupes are ignored).

    Parameters:
        my_list : list of integers (with possible dupes).

    Returns : the sum of unique integers from the list.
    """
    res = 0
    for i in set(my_list):
        res += i
    return res

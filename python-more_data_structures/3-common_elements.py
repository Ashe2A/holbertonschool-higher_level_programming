#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Adds all distinct integers from a list (meaning dupes are ignored).

    Parameters:
        my_list : list of integers (with possible dupes).

    Returns : the sum of unique integers from the list.
    """
    return set_1 & set_2

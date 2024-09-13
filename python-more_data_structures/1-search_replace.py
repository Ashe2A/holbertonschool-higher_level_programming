#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Square of matrix.

    Parameters:
        my_list : initial list
        search : element to replace in the list
        replace : new element

    Returns : the squared (or not) matrix
    """
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list

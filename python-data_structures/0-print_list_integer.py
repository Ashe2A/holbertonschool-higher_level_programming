#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints a list of integers SPECIFICALLY.

    Parameters:
        my_list (list) : the list.
    """
    for i in my_list:
        print("{:d}".format(i))

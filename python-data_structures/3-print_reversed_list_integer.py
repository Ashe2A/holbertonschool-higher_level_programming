#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints (in reverse) a list of integers SPECIFICALLY.

    Parameters:
        my_list (list) : the list.
    """
    if len(my_list) > 0:
        for i in my_list:
            print("{:d}".format(my_list[len(my_list) - 1 - i]))
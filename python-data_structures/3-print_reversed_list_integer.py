#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Reverse prints integers from a list.

    Args:
        my_list (list, optional): The list. Defaults to empty list.
    '''
    for i in reversed(my_list):
        print('{:d}'.format(i))

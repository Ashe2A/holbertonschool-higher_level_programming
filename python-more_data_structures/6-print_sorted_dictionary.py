#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Sort and print dictionary.

    Parameters:
        a_dictionary : the dictionary.
    """
    for i in a_dictionary:
        print("{}: {}".format(i[0], i[1]))
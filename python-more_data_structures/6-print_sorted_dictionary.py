#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Sort dictionary

    Args:
        a_dictionary (dict): The dictionary
    """
    if a_dictionary is not None:
        for i in sorted(a_dictionary):
            print("{}: {}".format(i, a_dictionary[i]))

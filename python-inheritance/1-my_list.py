#!/usr/bin/python3
"""
My list.
"""


class MyList(list):
    """My own version of a list

    Args:
        list (list): Extends from a list
    """

    def print_sorted(self):
        """Sort and print my list"""
        print(sorted(self))

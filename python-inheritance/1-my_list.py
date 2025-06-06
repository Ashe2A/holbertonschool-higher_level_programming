#!/usr/bin/python3
"""My list"""


class MyList(list):
    """My list class

    Args:
        list (list): Inherits from lists
    """

    def print_sorted(self):
        """Sort and print the list"""
        print(sorted(self))

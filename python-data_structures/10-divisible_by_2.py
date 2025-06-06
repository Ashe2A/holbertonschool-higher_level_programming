#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Even or odd ?

    Args:
        my_list (list, optional): List of numbers. Defaults to empty list.

    Returns:
        list(bool): Corresponding list of whether the numbers are odd or even
    """
    even_or_odd = []
    for i in my_list:
        even_or_odd.append(i % 2 == 0)
    return even_or_odd

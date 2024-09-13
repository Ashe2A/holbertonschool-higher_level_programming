#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Unify elements from two sets.

    Parameters:
        set_1 : first set.
        set_2 : second set.

    Returns :
        Distinct elements between the sets.
    """
    return set_1 ^ set_2

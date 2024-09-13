#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add a tuple.

    Parameters:
        tuple_a (tuple) : first tuple.
        tuple_b (tuple) : second tuple.

    Returns:
        Tuple (int, int) : sum of first elements, sum of second elements
    """
    res = (0, 0)
    if tuple_a != ():
        res[0] += tuple_a[0]
    if tuple_b != ():
        res[0] += tuple_b[0]
    if len(tuple_a) >= 2:
        res[1] += tuple_a[1]
    if len(tuple_b) >= 2:
        res[1] += tuple_b[1]
    return res

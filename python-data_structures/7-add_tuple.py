#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''Sums tuples together

    Args:
        tuple_a (tuple, optional): The first tuple. Defaults to empty tuple.
        tuple_b (tuple, optional): The second tuple. Defaults to empty tuple.

    Returns:
        The summed up tuple
    '''
    res_zero = 0
    res_one = 0
    if len(tuple_a) > 0:
        res_zero += tuple_a[0]
    if len(tuple_a) >= 2:
        res_one += tuple_a[1]
    if len(tuple_b) > 0:
        res_zero += tuple_b[0]
    if len(tuple_b) >= 2:
        res_one += tuple_b[1]
    return (res_zero, res_one)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_add = 0
    second_add = 0
    if len(tuple_a) >= 1:
        first_add += tuple_a[0]
    if len(tuple_b) >= 1:
        first_add += tuple_b[0]
    if len(tuple_a) >= 2:
        second_add += tuple_a[1]
    if len(tuple_b) >= 2:
        second_add += tuple_b[1]
    return (first_add, second_add)

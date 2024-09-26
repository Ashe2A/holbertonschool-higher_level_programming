#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safe print list.
    """
    res = 0
    for i in range(x):
        try:
            print(my_list[x])
            res += 1
        except:
            print("Out of bonds")
    return res

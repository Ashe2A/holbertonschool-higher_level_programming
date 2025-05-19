#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Prints a list up to a certain number of integers

    Args:
        my_list (list, optional): The list. Defaults to empty list.
        x (int, optional): Number of elements to access. Defaults to 0.

    Returns:
        int: The number of integers actually printed
    '''
    nb_print = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            nb_print += 1
        except (TypeError, ValueError):
            continue
    print()
    return nb_print

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints a list up to a certain number of elements

    Args:
        my_list (list, optional): The list. Defaults to empty list.
        x (int, optional): Number of elements printed. Defaults to 0.

    Returns:
        int: The number of elements actually printed
    """
    try:
        nb_print = 0
        for i in my_list:
            if nb_print <= x - 1:
                print(i, end="")
                nb_print += 1
        print()
        return nb_print
    except Exception as e:
        print(e)

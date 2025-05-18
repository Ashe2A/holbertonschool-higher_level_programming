#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
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

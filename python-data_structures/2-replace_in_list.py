#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (0 < idx < len(my_list)) and (len(my_list) > 0):
        my_list[idx] = element
    else:
        return my_list

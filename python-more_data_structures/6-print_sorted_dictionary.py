#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_list = []
    for i in a_dictionary:
        dic_list.append(f"{i}: {a_dictionary[i]}")
    dic_list.sort()
    for i in dic_list:
        print("{}".format(i))

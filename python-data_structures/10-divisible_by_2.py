#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    evenoddlist = []
    for i in my_list:
        if i % 2 == 0:
            evenoddlist.append(True)
        else:
            evenoddlist.append(False)
    return evenoddlist

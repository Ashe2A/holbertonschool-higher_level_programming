#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    uniq_int = []
    unique = True
    for i in my_list:
        for j in uniq_int:
            unique = True
            if j == i:
                unique = False
                break
        if unique:
            uniq_int.append(i)
            res += i
    return res

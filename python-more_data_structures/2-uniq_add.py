#!/usr/bin/python3
def common_elements(set_1, set_2):
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

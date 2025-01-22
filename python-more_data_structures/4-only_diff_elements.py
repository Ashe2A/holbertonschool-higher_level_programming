#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = []
    common = False
    for i in set_1:
        common = False
        for j in set_2:
            if i == j:
                common = True
                break
        if not common:
            diff_set.append(i)
    for i in set_2:
        common = False
        for j in set_1:
            if i == j:
                common = True
                break
        if not common:
            diff_set.append(i)
    return diff_set

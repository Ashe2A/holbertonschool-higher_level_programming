#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common_set.append(i)
                break
    return common_set

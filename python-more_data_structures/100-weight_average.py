#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    weight = 0
    if my_list == []:
        return 0
    else:
        for i in my_list:
            total += i[0] * i[1]
            weight += i[1]
        return total / weight

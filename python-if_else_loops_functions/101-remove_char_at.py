#!/usr/bin/python3

def remove_char_at(str, n):
    str2 = ""
    j = 0
    for i in str:
        if j != n:
            str2 += i
        j += 1
    return str2
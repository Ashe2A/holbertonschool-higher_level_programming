#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if ord("a") <= ord(i) <= ord("z"):
            res += chr(ord(i) + ord("A") - ord("a"))
        else:
            res += i
    print(res)

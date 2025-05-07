#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord("a") <= ord(i) <= ord("z"):
            i = chr(ord(i) + ord("A") - ord("a"))
        print("{}".format(i), end="")
    print()

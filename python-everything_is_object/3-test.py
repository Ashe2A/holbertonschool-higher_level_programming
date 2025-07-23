#!/usr/bin/python3
a = 89
b = 89

with open("3-answer.txt", "w") as f:
    if id(a) == id(b):
        f.write("Yes\n")
    else:
        f.write("No\n")

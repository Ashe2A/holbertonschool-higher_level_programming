#!/usr/bin/python3
"""Tests for Right count = (4)"""
a = 89
b = a

with open("4-answer.txt", "w") as f:
    """If a and b point to the same adress,
    write Yes in 4-answer.txt, otherwise No"""
    if id(a) == id(b):
        f.write("Yes\n")
    else:
        f.write("No\n")

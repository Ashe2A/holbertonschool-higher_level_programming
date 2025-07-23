#!/usr/bin/python3
"""Tests for Right count ="""
a = 89
b = 89

with open("3-answer.txt", "w") as f:
    """If a and b point to the same adress,
    write Yes in 3-answer.txt, otherwise No"""
    if id(a) == id(b):
        f.write("Yes\n")
    else:
        f.write("No\n")

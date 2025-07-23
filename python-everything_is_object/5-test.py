#!/usr/bin/python3
"""Tests for Right count =+"""
a = 89
b = a + 1

with open("5-answer.txt", "w") as f:
    """If a and b point to the same adress,
    write Yes in 5-answer.txt, otherwise No"""
    if id(a) == id(b):
        f.write("Yes\n")
    else:
        f.write("No\n")

#!/usr/bin/python3
"""Tests for Tuple or not? (21)"""
a = (1, 2)

with open("21-answer.txt", "w") as f:
    """If a is a tuple,
    write Yes in 21-answer.txt, otherwise No"""
    if type(a) == tuple:
        f.write("Yes\n")
    else:
        f.write("No\n")

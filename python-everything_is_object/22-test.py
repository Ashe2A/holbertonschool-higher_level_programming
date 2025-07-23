#!/usr/bin/python3
"""Tests for Tuple or not? (22)"""
a = (1)

with open("22-answer.txt", "w") as f:
    """If a is a tuple,
    write Yes in 22-answer.txt, otherwise No"""
    if type(a) == tuple:
        f.write("Yes\n")
    else:
        f.write("No\n")

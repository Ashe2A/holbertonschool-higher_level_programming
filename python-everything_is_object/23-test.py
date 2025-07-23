#!/usr/bin/python3
"""Tests for Tuple or not? (23)"""
a = (1, )

with open("23-answer.txt", "w") as f:
    """If a is a tuple,
    write Yes in 23-answer.txt, otherwise No"""
    if type(a) == tuple:
        f.write("Yes\n")
    else:
        f.write("No\n")

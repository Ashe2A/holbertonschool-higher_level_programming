#!/usr/bin/python3
"""Tests for Tuple or not? (20)"""
a = ()

with open("20-answer.txt", "w") as f:
    """If a is a tuple,
    write Yes in 20-answer.txt, otherwise No"""
    if type(a) == tuple:
        f.write("Yes\n")
    else:
        f.write("No\n")

#!/usr/bin/python3
"""Tests for Tuple or not"""
a = (1, 2)
b = (1, 2)

with open("25-answer.txt", "w") as f:
    """Write whether a and b are the same object in 25-answer.txt"""
    f.write("{}\n".format(a is b))

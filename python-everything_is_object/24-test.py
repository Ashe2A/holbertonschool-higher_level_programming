#!/usr/bin/python3
"""Tests for Who I am?"""
a = (1)
b = (1)

with open("24-answer.txt", "w") as f:
    """Write whether a and b are the same object in 24-answer.txt"""
    f.write("{}\n".format(a is b))

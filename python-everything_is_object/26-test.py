#!/usr/bin/python3
"""Tests for Empty is not empty"""
a = ()
b = ()

with open("26-answer.txt", "w") as f:
    """Write whether a and b are the same object in 26-answer.txt"""
    f.write("{}\n".format(a is b))

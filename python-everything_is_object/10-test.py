#!/usr/bin/python3
"""Tests for And with a list, is it equal"""
l1 = [1, 2, 3]
l2 = [1, 2, 3]

with open("10-answer.txt", "w") as f:
    """Print whether s1 and s2 are equal in 10-answer.txt"""
    f.write("{}\n".format(l1 == l2))

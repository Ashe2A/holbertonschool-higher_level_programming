#!/usr/bin/python3
"""Tests for And with a list, is it really the same"""
l1 = [1, 2, 3]
l2 = l1

with open("13-answer.txt", "w") as f:
    """Print whether s1 and s2 are the same object in 13-answer.txt"""
    f.write("{}\n".format(l1 is l2))

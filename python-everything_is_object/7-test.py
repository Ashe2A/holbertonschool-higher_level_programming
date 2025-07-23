#!/usr/bin/python3
"""Tests for Is the same"""
s1 = "Best School"
s2 = s1

with open("7-answer.txt", "w") as f:
    """Print whether s1 and s2 are the same object in 7-answer.txt"""
    f.write("{}\n".format(s1 is s2))

#!/usr/bin/python3
"""Tests for Is equal"""
s1 = "Best School"
s2 = s1

with open("6-answer.txt", "w") as f:
    """Print whether s1 and s2 are equal in 6-answer.txt"""
    f.write("{}\n".format(s1 == s2))

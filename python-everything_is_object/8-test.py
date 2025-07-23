#!/usr/bin/python3
"""Tests for Is really equal"""
s1 = "Best School"
s2 = "Best School"

with open("7-answer.txt", "w") as f:
    """Print whether s1 and s2 are equal in 7-answer.txt"""
    f.write("{}\n".format(s1 == s2))

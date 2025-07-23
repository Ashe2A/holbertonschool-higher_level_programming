#!/usr/bin/python3
"""Tests for Is really the same"""
s1 = "Best School"
s2 = "Best School"

with open("9-answer.txt", "w") as f:
    """Print whether s1 and s2 are the same object in 9-answer.txt"""
    f.write("{}\n".format(s1 is s2))

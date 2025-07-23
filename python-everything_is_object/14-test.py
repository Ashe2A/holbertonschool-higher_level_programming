#!/usr/bin/python3
"""Tests for List append"""
l1 = [1, 2, 3]
l2 = l1
l1.append(4)

with open("14-answer.txt", "w") as f:
    """Print l2 (check whether 4 has been appended to l2 just like l1)
    in 14-answer.txt"""
    f.write("{}\n".format(l2))

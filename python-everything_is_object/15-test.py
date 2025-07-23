#!/usr/bin/python3
"""Tests for List add"""
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]

with open("15-answer.txt", "w") as f:
    """Print l2 (check whether 4 has been appended to l2 with list adding)
    in 15-answer.txt"""
    f.write("{}\n".format(l2))

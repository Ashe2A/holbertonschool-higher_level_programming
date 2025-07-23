#!/usr/bin/python3
"""Tests for Same or not?"""
a = [1, 2, 3]
id_a = id(a)
a += [4]
new_id_a = id(a)

with open("28-answer.txt", "w") as f:
    """Write whether a keeps the same address
    upon being incremented a value in 28-answer.txt"""
    if id_a == new_id_a:
        f.write("Yes\n")
    else:
        f.write("No\n")

#!/usr/bin/python3
"""Tests for Still the same?"""
a = [1, 2, 3, 4]
id_a = id(a)
a = a + [5]
new_id_a = id(a)

with open("27-answer.txt", "w") as f:
    """Write whether a keeps the same address
    upon being added a value in 27-answer.txt"""
    if id_a == new_id_a:
        f.write("Yes\n")
    else:
        f.write("No\n")

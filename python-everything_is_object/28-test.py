#!/usr/bin/python3
"""Tests for Same or not?"""
a = [1, 2, 3]
id_a = id(a)
print("a id: {}".format(id_a))
a += [4]
new_id_a = id(a)
print("a new id: {}".format(new_id_a))
print("Are both id the same?: {}".format(id_a == new_id_a))

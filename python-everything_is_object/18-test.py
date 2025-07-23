#!/usr/bin/python3
"""Tests for List assignation"""
def assign_value(n, v):
    n = v


l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)

with open("18-answer.txt", "w") as f:
    """Print l1 (check whether l has been replaced with l2 using a method)
    in 18-answer.txt"""
    f.write("{}\n".format(l1))

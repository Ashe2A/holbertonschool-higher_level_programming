
#!/usr/bin/python3
"""Tests for Integer incrementation"""
def increment(n):
    n += 1


a = 1
increment(a)

with open("16-answer.txt", "w") as f:
    """Print a (check whether it has been incremented using a method)
    in 16-answer.txt"""
    f.write("{}\n".format(a))

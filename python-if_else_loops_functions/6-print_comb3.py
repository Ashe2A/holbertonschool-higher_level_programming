#!/usr/bin/python3
for i in range(0, 100):
    if (i / 10) < (i % 10):
        if i == 89:
            print(i)
        else:
            if i < 10:
                print("0", end="")
            print(i, end=", ")

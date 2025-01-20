#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        firstcol = True
        for j in i:
            if firstcol is True:
                firstcol = False
            else:
                print("", end=" ")
            print("{:d}".format(j), end="")
        print()

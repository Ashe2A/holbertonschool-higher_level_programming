#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if (not (roman_string is None)) and isinstance(roman_string, str):
        for i in roman_string:
            if (i == "M"):
                res += 1000
                if (i - 1 == "C"):
                    res -= 100
            if (i == "D"):
                res += 500
                if (i - 1 == "C"):
                    res -= 100
            if (i == "C"):
                res += 100
                if (i - 1 == "X"):
                    res -= 10
            if (i == "L"):
                res += 50
                if (i - 1 == "X"):
                    res -= 10
            if (i == "X"):
                res += 10
                if (i - 1 == "I"):
                    res -= 1
            if (i == "V"):
                res += 5
                if (i - 1 == "I"):
                    res -= 1
            if (i == "I"):
                res += 1
        return res
    else:
        return 0

#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if not (roman_string is None) and isinstance(roman_string, str):
        for i in roman_string:
            if (i is "M"):
                res += 1000
                if (i - 1 is "C"):
                    res -= 100
            if (i is "D"):
                res += 500
                if (i - 1 is "C"):
                    res -= 100
            if (i is "C"):
                res += 100
                if (i - 1 is "X"):
                    res -= 10
            if (i is "L"):
                res += 50
                if (i - 1 is "X"):
                    res -= 10
            if (i is "X"):
                res += 10
                if (i - 1 is "I"):
                    res -= 1
            if (i is "V"):
                res += 5
                if (i - 1 is "I"):
                    res -= 1
            if (i is "I"):
                res += 1
        return res
    else:
        return 0

#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    for i in range(len(roman_string)):
        if roman_string[i] == "M":
            res += 1000
            continue
        if roman_string[i] == "D":
            res += 500
            continue
        if roman_string[i] == "C":
            if i + 1 < len(roman_string) and roman_string[i + 1] == "D":
                res += 400
                i += 1
                continue
            elif i + 1 < len(roman_string) and roman_string[i + 1] == "M":
                res += 900
                i += 1
                continue
            else:
                res += 100
                continue
        if roman_string[i] == "L":
            res += 50
            continue
        if roman_string[i] == "X":
            if i + 1 < len(roman_string) and roman_string[i + 1] == "L":
                res += 40
                i += 1
                continue
            elif i + 1 < len(roman_string) and roman_string[i + 1] == "C":
                res += 90
                i += 1
                continue
            else:
                res += 10
                continue
        if roman_string[i] == "V":
            res += 5
            continue
        if roman_string[i] == "I":
            if i + 1 < len(roman_string) and roman_string[i + 1] == "V":
                res += 4
                break
            elif i + 1 < len(roman_string) and roman_string[i + 1] == "X":
                res += 9
                break
            else:
                res += 1
    return res

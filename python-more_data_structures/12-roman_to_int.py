#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    i = 0
    if roman_string is not None and isinstance(roman_string, str):
        while i < len(roman_string):
            if roman_string[i] == "M":
                res += 1000
            if roman_string[i] == "D":
                res += 500
            if roman_string[i] == "C":
                if i + 1 < len(roman_string) and roman_string[i + 1] == "D":
                    res += 400
                    i += 1
                elif i + 1 < len(roman_string) and roman_string[i + 1] == "M":
                    res += 900
                    i += 1
                else:
                    res += 100
            if roman_string[i] == "L":
                res += 50
            if roman_string[i] == "X":
                if i + 1 < len(roman_string) and roman_string[i + 1] == "L":
                    res += 40
                    i += 1
                elif i + 1 < len(roman_string) and roman_string[i + 1] == "C":
                    res += 90
                    i += 1
                else:
                    res += 10
            if roman_string[i] == "V":
                res += 5
            if roman_string[i] == "I":
                if i + 1 < len(roman_string) and roman_string[i + 1] == "V":
                    res += 4
                    break
                elif i + 1 < len(roman_string) and roman_string[i + 1] == "X":
                    res += 9
                    break
                else:
                    res += 1
            i += 1
    return res

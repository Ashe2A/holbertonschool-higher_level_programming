#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if (not (roman_string is None)) and isinstance(roman_string, str):
        for i in range(len(roman_string)):
            if (roman_string[i] == "M"):
                res += 1000
                if (roman_string[i - 1] == "C"):
                    res -= 100
            elif (roman_string[i] == "D"):
                res += 500
                if (roman_string[i - 1] == "C"):
                    res -= 100
            elif (roman_string[i] == "C"):
                res += 100
                if (roman_string[i - 1] == "X"):
                    res -= 10
            elif (roman_string[i] == "L"):
                res += 50
                if (roman_string[i - 1] == "X"):
                    res -= 10
            elif (roman_string[i] == "X"):
                res += 10
                if (roman_string[i - 1] == "I"):
                    res -= 1
            elif (roman_string[i] == "V"):
                res += 5
                if (roman_string[i - 1] == "I"):
                    res -= 1
            elif (roman_string[i] == "I"):
                res += 1
        return res
    else:
        return 0

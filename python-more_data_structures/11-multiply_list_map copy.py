#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if not ((roman_string is None) or (roman_string is not str)):
        milium = True
        for i in roman_string:
            if (i == 'M') and milium:
                if (i != 0) and (i - 1 == 'C'):
                    res += 900
                else:
                    res += 1000
            else:
                return 0
        return res
    return 0


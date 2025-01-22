#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    rs = roman_string
    if not isinstance(rs, str) or rs is None:
        return 0
    else:
        for i in range(len(rs)):
            if rs[i] == "M":
                result += 1000
            if rs[i] == "D":
                result += 500
            if rs[i] == "C":
                if i < len(rs) - 1 \
                      and (rs[i + 1] == "M" or rs[i + 1] == "D"):
                    result -= 100
                else:
                    result += 100
            if rs[i] == "L":
                result += 50
            if rs[i] == "X":
                if i < len(rs) - 1 \
                      and (rs[i + 1] == "C" or rs[i + 1] == "L"):
                    result -= 10
                else:
                    result += 10
            if rs[i] == "V":
                result += 5
            if rs[i] == "I":
                if i < len(rs) - 1 \
                      and (rs[i + 1] == "V" or rs[i + 1] == "X"):
                    result -= 1
                else:
                    result += 1
        return result

#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
        except Exception:
            pass
        else:
            result += (a ** b) / i
        result = b + a
    return result

print(magic_calculation(1, 2))
print(magic_calculation(1, 4))
print(magic_calculation(4, 1))
print(magic_calculation(3, 3))
print(magic_calculation(1, 1))

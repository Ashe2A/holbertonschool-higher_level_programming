#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    argc = len(argv)
    if argc == 4:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if argv[2] == "+":
            result = add(a, b)
        elif argv[2] == "-":
            result = sub(a, b)
        elif argv[2] == "*":
            result = mul(a, b)
        elif argv[2] == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(a, operator, b, result))
        exit(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

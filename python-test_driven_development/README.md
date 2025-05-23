# [Python - Test-driven development](https://intranet.hbtn.io/projects/2123)
**Note:** Execute test files with `python3 -m doctest -v <test file path>`

## 0. Integers addition
### [`0-add_integer.py`](0-add_integer.py)
* Function that sums up two integers, or integer-casted floats, and raises `TypeError` when it's neither. Avoided module importing.
### [See test file](tests/0-add_integer.txt)

## 1. Divide a matrix
### [`2-matrix_divided.py`](2-matrix_divided.py)
* Function that divides up a matrix with an integer, or integer-casted float, and raises `TypeError` when it's neither, or `ZeroDivisionError` when it's `0`, by returning a new matrix. Avoided module importing.
### [See test file](tests/2-matrix_divided.txt)

## 2. Say my name
### [`3-say_my_name.py`](3-say_my_name.py)
* Function that prints a full name and raises `TypeError` when they're not strings. Avoided module importing.
### [See test file](tests/3-say_my_name.txt)

## 3. Print square
### [`4-print_square.py`](4-print_square.py)
* Function that prints a square and raises `TypeError` when the specified size is not an integer, and `ValueError` when it's negative. Avoided module importing.
### [See test file](tests/4-print_square.txt)

## 4. Text indentation
### [`5-text_indentation.py`](5-text_indentation.py)
* Function that prints a string with a newline each `.`, `?` and `:` character. It raises `TypeError` when the text to indent isn't a string. Avoided module importing and removed newline early spaces.
### [See test file](tests/5-text_indentation.txt)

## 5. Max integer - Unittest
### [`6-max_integer.py`](6-max_integer.py)
* Function that find and return the max integer in a list of integers. If the list is empty, the function returns `None`.
* Note: The file is already created and only unit tests have been implemented.
### [See unit test file](tests/6-max_integer_test.txt)
* Note: Test with `python3 -m unittest tests.6-max_integer_test`
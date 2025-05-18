# [Python - Exceptions](https://intranet.hbtn.io/projects/2122)

## 0. Safe list printing
### [`0-safe_print_list.py`](0-safe_print_list.py)
* Function that prints a list in the same line, up to a certain number of elements and returns the number of printed elements. Avoided module importing or `len()`. Used `try`/`except`.
### [`0-main.py`](0-main.py)
* **Tests:**
    * `[1, 2, 3, 4, 5]` and `2` should print `12` and return `2`
    * `[1, 2, 3, 4, 5]` and `5` should print `12345` and return `5`
    * `[1, 2, 3, 4, 5]` and `7` should print `12345` and return `5`

## 1. Safe printing of an integers list
### [`1-safe_print_integer.py`](1-safe_print_integer.py)
* Function that prints a list in the same line, up to a certain number of elements and returns the number of printed elements. Avoided module importing or `type()`. Used `try`/`except` and `"{:d}".format()`.
### [`1-main.py`](1-main.py)
* **Tests:**
    * `89` should print `89` and return `True`
    * `-89` should print `-89` and return `True`
    * `"School"` should return `False`

## 2. Print and count integers
### [`2-safe_print_list_integers.py`](2-safe_print_list_integers.py)
* Function that prints a list in the same line, up to a certain number of integers (skips other type of elements) and returns the number of printed elements. Avoided module importing or `len()`. Used `try`/`except` and `"{:d}".format()`.
### [`2-main.py`](2-main.py)
* **Tests:**
    * `[1, 2, 3, 4, 5]` and `2` should print `12` and return `2`
    * `[1, 2, 3, 4, 5]` and `5` should print `12345` and return `5`
    * `[1, 2, 3, 4, 5]` and `7` should print `12345` and an `IndexError` message

## 3. Integers division with debug
### [`3-safe_print_division.py`](3-safe_print_division.py)
* Function that returns a float division result and prints `Inside result: ` with the result. Avoided module importing. Used `try`/`except`/`finally` and `"{}".format()`.
### [`3-main.py`](3-main.py)
* **Tests:**
    * `12` and `2` should return `6.0` and print `Inside result: 6.0`
    * `12` and `0` should return `None` and print `Inside result: None`
* Note: `a` and `b` should be integers

## 4. Divide a list
### [`4-list_division.py`](4-list_division.py)
* Function that returns a list of float division results between lists and prints `wrong type` when an element is not an int or float, `division by 0` when there's a zero division, and `out of range` when the new list length is higher than any of the lists'. Avoided module importing. Used `try`/`except`/`finally`.
### [`4-main.py`](4-main.py)
* **Tests:**
    * `[10, 8, 4]` and `[2, 4, 4]` with `3` should return `[5.0, 2.0, 1.0]`
    * `[10, 8, 4, 4]` and `[2, 0, "H", 2, 7]` with `5` should return `[5.0, 0, 0, 2.0, 0]` and print `division by 0`, `wrong type`, `out of range`

## 5. Raise exception
### [`5-raise_exception.py`](5-raise_exception.py)
* Raise type error exception. Avoided module importing.
### [`5-main.py`](5-main.py)
* **Test:** Prints `"Exception raised"` when the exception is raised.

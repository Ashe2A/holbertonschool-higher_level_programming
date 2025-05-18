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
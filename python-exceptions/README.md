# [Python - Exceptions](https://intranet.hbtn.io/projects/2122)

## 0. Safe list printing
### [`0-safe_print_list.py`](0-safe_print_list.py)
* Function that prints a list in the same line, up to a certain number of elements and returns the number of printed elements. Avoided module importing or `len()`. Used `try`/`except`.
### [`0-main.py`](0-main.py)
* **Tests:**
    * `[1, 2, 3, 4, 5]` and `2` should print `12` and return `2`
    * `[1, 2, 3, 4, 5]` and `5` should print `12345` and return `5`
    * `[1, 2, 3, 4, 5]` and `7` should print `12345` and return `5`

# [Python - Test-driven development](https://intranet.hbtn.io/projects/2123)

## 0. Integers addition
### [`0-add_integer.py`](0-add_integer.py)
* Function that sums up two integers, or integer-casted floats, and raises `TypeError` when it's neither. Avoided module importing.
### [`0-main.py`](0-main.py)
* **Tests:**
    * `1` and `2` should return `3`
    * `100` and `-2` should return `98`
    * `2` should return `100`
    * `100.3` and `-2` should return `98`
    * `4` and `"School"` should return `"b must be an integer"`
    * `None` should return `"a must be an integer"`
### [See test file](tests/0-add_integer.txt)

## 1. Divide a matrix
### [`2-matrix_divided.py`](2-matrix_divided.py)
* Function that divides up a matrix with an integer, or integer-casted float, and raises `TypeError` when it's neither, or `ZeroDivisionError` when it's `0`, by returning a new matrix. Avoided module importing.
### [`2-main.py`](2-main.py)
* **Tests:**
    * `[[1, 2, 3], [4, 5, 6]]` and `3` should return `[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]`
    * `[[1, 2, 3], [4, 5, 6]]` alone should return `[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]`
### [See test file](tests/2-matrix_divided.txt)

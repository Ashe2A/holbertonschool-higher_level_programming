# [Python - Test-driven development](https://intranet.hbtn.io/projects/2123)

## 0. Integers addition
### [`0-add_integer.py`](0-add_integer.py)
* Function that sums up two integers, or integer-casted floats, and raises `TypeError` when it"s neither. Avoided module importing.
### [`0-main.py`](0-main.py)
* **Tests:**
    * `1` and `2` should return `3`
    * `100` and `-2` should return `98`
    * `2` should return `100`
    * `100.3` and `-2` should return `98`
    * `4` and `"School"` should return `"b must be an integer"`
    * `None` should return `"a must be an integer"`
### [See test file](tests/0-add_integer.txt)

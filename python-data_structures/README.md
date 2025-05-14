# [Python - data_structures](https://intranet.hbtn.io/projects/2120)

## 0. Print a list of integers
### [`0-print_list_integer.py`](0-print_list_integer.py)
* Function that prints a list of integers (one each line). Avoided module import as well as integer-casting, and used the `.format()` method.
### [`0-main.py`](0-main.py)
* **Test:** `[1, 2, 3, 4, 5]` should print `1`, `2`, `3`, `4` and `5` ending each with a new line
* Note : Every list should be made of integers, and the `:d` format is enforced.

## 1. Secure access to an element in a list
### [`1-element_at.py`](1-element_at.py)
* Function that retrives an element from a list. Avoided module import as well as `try`/`except`.
### [`1-main.py`](1-main.py)
* **Test:** Element at index 3 of `[1, 2, 3, 4, 5]` should be `4`.
* Note : Out of range index should retrieve `None`

## 2. Replace element
### [`2-replace_in_list.py`](2-replace_in_list.py)
* Function that replaces an element in a list and returns the list (modified or not). Avoided module import as well as `try`/`except`.
### [`2-main.py`](2-main.py)
* **Test:** Element at index 3 of `[1, 2, 3, 4, 5]` can be replaced by `9`.
* Note : Out of range index should not rewrite anything

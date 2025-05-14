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

## 3. Print a list of integers... in reverse!
### [`3-print_reversed_list_integer.py`](3-print_reversed_list_integer.py)
* Function that prints a list of integers (one each line) backwards. Avoided module import as well as integer-casting, and used the `.format()` method.
### [`3-main.py`](3-main.py)
* **Test:** `[1, 2, 3, 4, 5]` should print `5`, `4`, `3`, `2` and `1` ending each with a new line
* Note : Every list should be made of integers, and the `:d` format is enforced.

## 4. Replace in a copy
### [`4-new_in_list.py`](4-new_in_list.py)
* Function that replaces an element in a list and returns a modified copy of the list. Avoided module import as well as `try`/`except`.
### [`4-main.py`](4-main.py)
* **Test:** Element at index 3 of `[1, 2, 3, 4, 5]` can be replaced by `9` in the new list.
* Note : Out of range index should not rewrite anything

## 5. Can you C me now?
### [`5-no_c.py`](5-no_c.py)
* Function that removes Cs (lowercase or uppercase) from a string (returns a modified copy of the string). Avoided module import as well as the `replace()` method.
### [`5-main.py`](5-main.py)
* **Tests:**
    * `"Best School"` should return `"Best Shool"`
    * `"Chicago"` should return `"hiago"`
    * `"C is fun!"` should return `" is fun!"`

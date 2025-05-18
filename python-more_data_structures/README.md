# [Python - More Data Structures: Set, Dictionary](https://intranet.hbtn.io/projects/2121)

## 0. Squared simple
### [`0-print_list_integer.py`](0-print_list_integer.py)
* Function that squares up the integers in a matrix. Avoided module import and mapping loops.
### [`0-main.py`](0-main.py)
* **Test:** `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` should return `[[1, 4, 9], [16, 25, 36], [49, 64, 81]]`.
* Note: Every list should be made of integers, and the original matrix stays untouched.

## 1. Search and replace
### [`1-search_replace.py`](1-search_replace.py)
* Function that replaces all occurrences of an element in a list by another. Avoided module import.
### [`1-main.py`](1-main.py)
* **Test:** `[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]` with `89` replacing every `2` should return `[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]`.
* Note: The original matrix stays untouched.

## 2. Unique addition
### [`2-uniq_add.py`](2-uniq_add.py)
* Function that adds all unique integers in a list. Avoided module import.
### [`2-main.py`](2-main.py)
* **Test:** `[1, 2, 3, 1, 4, 2, 5]` should return `15`.
* Note: Every list should be made of integers.

## 3. Present in both
### [`3-common_elements.py`](3-common_elements.py)
* Function that intersects sets. Avoided module import.
### [`3-main.py`](3-main.py)
* **Test:** `{"Python", "C", "Javascript"}` and `{"Bash", "C", "Ruby", "Perl"}` should return `{"C"}`.

## 4. Only differents
### [`4-only_diff_elements.py`](4-only_diff_elements.py)
* Function that unifies sets (without intersects). Avoided module import.
### [`4-main.py`](4-main.py)
* **Test:** `{"Python", "C", "Javascript"}` and `{"Bash", "C", "Ruby", "Perl"}` should return `{"Bash", "Javascript", "Perl", "Python", "Ruby"}`.

## 5. Number of keys
### [`5-number_keys.py`](5-number_keys.py)
* Function that counts keys in a dictionary. Avoided module import.
### [`5-main.py`](5-main.py)
* **Test:** `{"language": "C", "number": 13, "track": "Low level"}` should return `3`.

## 6. Print sorted dictionary
### [`7-update_dictionary.py`](7-update_dictionary.py)
* Function that replaces/adds a key/value in a dictionary and returns it. Avoided module import.
### [`7-main.py`](7-main.py)
* **Test:** `{"language": "C", "number": 89, "track": "Low level"}` with the `'language': "Python"` key/value should return `{"language": "Python", "number": 89, "track": "Low level"}`.
* Note: Every key in the dictionary should be strings.

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
* **Test:** `{'Python', 'C', 'Javascript'}` and `{'Bash', 'C', 'Ruby', 'Perl'}` should return `{'C'}`.

## 4. Only differents
### [`4-only_diff_elements.py`](4-only_diff_elements.py)
* Function that unifies sets (without intersects). Avoided module import.
### [`4-main.py`](4-main.py)
* **Test:** `{'Python', 'C', 'Javascript'}` and `{'Bash', 'C', 'Ruby', 'Perl'}` should return `{'Bash', 'Javascript', 'Perl', 'Python', 'Ruby'}`.

## 5. Number of keys
### [`5-number_keys.py`](5-number_keys.py)
* Function that counts keys in a dictionary. Avoided module import.
### [`5-main.py`](5-main.py)
* **Test:** `{'language': 'C', 'number': 13, 'track': 'Low level'}` should return `3`.

## 6. Print sorted dictionary
### [`6-print_sorted_dictionary.py`](6-print_sorted_dictionary.py)
* Function that prints a dictionary ordered alphabetically by keys. Avoided module import. Only first-level keys are sorted.
### [`6-main.py`](6-main.py)
* **Test:** `{'language': 'C', 'Number': 89, 'track': 'Low level', 'ids': [1, 2, 3]}` should return `3`.
* Note: Every keys in the dictionary should be strings.

## 7. Update dictionary
### [`7-update_dictionary.py`](7-update_dictionary.py)
* Function that replaces/adds a key/value in a dictionary and returns the updated dictionary. Avoided module import.
### [`7-main.py`](7-main.py)
* **Test:** `{'language': 'C', 'number': 89, 'track': 'Low level'}` with the `'language': 'Python'` key/value should return `{'language': 'Python', 'number': 89, 'track': 'Low level'}`.
* Note: Every key in the dictionary should be strings.

## 8. Simple delete by key
### [`8-simple_delete.py`](8-simple_delete.py)
* Function that removes a key/value in a dictionary and returns the updated dictionary. Avoided module import and deleting when the key doesn't exist.
### [`8-main.py`](8-main.py)
* **Test:** `{'language': 'C', 'number': 89, 'track': 'Low', 'ids': [1, 2, 3]}` with the `'track'` key should return `{'language': 'C', 'number': 89, 'ids': [1, 2, 3]}`.
* Note: Every key should be strings.

## 9. Multiply by 2
### [`9-multiply_by_2.py`](9-multiply_by_2.py)
* Function that doubles values in a dictionary and returns an updated copy of the dictionary. Avoided module import.
### [`9-main.py`](9-main.py)
* **Test:** `{'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}` should return `{'John': 24, 'Alex': 16, 'Bob': 28, 'Mike': 28, 'Molly': 32}`.
* Note: Every value in the dictionary should be integers.

## 10. Best score
### [`10-best_score.py`](10-best_score.py)
* Function that finds the key of the highest value. Avoided module import. Returns `None` when there is no score.
### [`10-main.py`](10-main.py)
* **Test:** `{'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}` should return `'Molly'`.
* Note: Every value in the dictionary should be integers.

## 11. Multiply by using map
### [`11-multiply_list_map.py`](11-multiply_list_map.py)
* Function that maps a list by multiplying the elements by a number and converts it back to list format. Avoided module import, loops, modifying the original list and writing more than 3 lines.
### [`11-main.py`](11-main.py)
* **Test:** `[1, 2, 3, 4, 6]` and `4` should return `[4, 8, 12, 16, 24]`.

## 12. Roman to Integer
### [`12-roman_to_int.py`](12-roman_to_int.py)
* Function that maps a list by multiplying the elements by a number and converts it back to list format. Avoided module import, loops, modifying the original list and writing more than 3 lines.
### [`12-main.py`](12-main.py)
* **Tests:**
    * `'X'` should return `10`
    * `'VII'` should return `7`
    * `'IX'` should return `9`
    * `'LXXXVII'` should return `87`
    * `'DCCVII'` should return `707`

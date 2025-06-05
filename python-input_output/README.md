# [Python - Input/Output](https://intranet.hbtn.io/projects/2182)

## 0. Read file
### [`0-read_file.py`](0-read_file.py)
* Read a file. Avoided module import and exceptions.
### [`0-main.py`](0-main.py)
* **Tests:** `my_file_0.txt` text file encoded in UTF-8

## 1. Write to a file
### [`1-write_file.py`](1-write_file.py)
* Write into a file, creates a file when non existent or overwrites its content if it exists. Returns the number of printed characters. Avoided module import and exceptions.
### [`1-main.py`](1-main.py)
* **Tests:** Write `my_first_file.txt` text file encoded in UTF-8

## 2. Append to a file
### [`2-append_write.py`](2-append_write.py)
* Write into a file, creates a file when non existent or appends to its content if it exists. Returns the number of printed characters. Avoided module import and exceptions.
### [`2-main.py`](2-main.py)
* **Tests:** `file_append.txt` text file encoded in UTF-8

## 3. To JSON string
### [`3-to_json_string.py`](3-to_json_string.py)
* Function that converts an object into a JSON dump.
### [`3-main.py`](3-main.py)
* **Tests:** List `[1, 2, 3]` and dictionary `{'id': 12, 'name': 'John', 'places': ['San Francisco', 'Tokyo'], 'is_active': True, 'info': {'age': 36, 'average': 3.14}}`

## 4. From JSON string to Object
### [`4-from_json_string.py`](4-from_json_string.py)
* Function that converts a JSON dump into a python object.
### [`4-main.py`](4-main.py)
* **Tests:** List `'[1, 2, 3]'` and dictionary `'''{'is_active': true, 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'name': 'John', 'places': ['San Francisco', 'Tokyo']}'''`

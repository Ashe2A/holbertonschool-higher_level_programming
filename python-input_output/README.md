# [Python - Input/Output](https://intranet.hbtn.io/projects/2182)

## 0. Read file
### [`0-read_file.py`](0-read_file.py)
* Function that reads a file. Avoided module import and exceptions.
### [`0-main.py`](0-main.py)
* **Tests:** [`my_file_0.txt`](my_file_0.txt) text file encoded in UTF-8

## 1. Write to a file
### [`1-write_file.py`](1-write_file.py)
* Function that writes into a file, creates a file when non existent or overwrites its content if it exists. Returns the number of printed characters. Avoided module import and exceptions.
### [`1-main.py`](1-main.py)
* **Tests:** Write [`my_first_file.txt`](my_first_file.txt) text file encoded in UTF-8

## 2. Append to a file
### [`2-append_write.py`](2-append_write.py)
* Function that writes into a file, creates a file when non existent or appends to its content if it exists. Returns the number of printed characters. Avoided module import and exceptions.
### [`2-main.py`](2-main.py)
* **Tests:** [`file_append.txt`](file_append.txt) text file encoded in UTF-8

## 3. To JSON string
### [`3-to_json_string.py`](3-to_json_string.py)
* Function that converts an object into a JSON dump. Avoided exceptions.
### [`3-main.py`](3-main.py)
* **Tests:** List `[1, 2, 3]` and dictionary `{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": True, "info": {"age": 36, "average": 3.14}}`

## 4. From JSON string to Object
### [`4-from_json_string.py`](4-from_json_string.py)
* Function that converts a JSON dump into a python object. Avoided exceptions.
### [`4-main.py`](4-main.py)
* **Tests:** List `"[1, 2, 3]"` and dictionary `"""{"is_active": true, "info": {"age": 36, "average": 3.14}, "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}"""`

## 5. Save Object to a file
### [`5-save_to_json_file.py`](5-save_to_json_file.py)
* Function that writes an object's JSON dump into a file. Avoided exceptions.
### [`5-main.py`](5-main.py)
* **Tests:** See [`my_list.json`](my_list.json), [`my_dict.json`](my_dict.json), [`my_set.json`](my_set.json) files
* Sets are not a JSON serializable object type

## 6. Create object from a JSON file
### [`6-load_from_json_file.py`](6-load_from_json_file.py)
* Function that creates an object's from its JSON dump. Avoided exceptions.
### [`6-main.py`](6-main.py)
* **Tests:** See [`my_list.json`](my_list.json), [`my_dict.json`](my_dict.json)

## 7. Load, add, save
### [`7-add_item.py`](7-add_item.py)
* Script that takes args and writes them into a JSON dump in a file.
* **Tests:**
    * No args writes `[]`
    * `"Best"` and `"School"` writes `["Best", "School"]`
    * `"89"`, `"School"` and `"C"` updates into `["Best", "School", "89", "Python", "C"]`

## 8. Class to JSON
### [`8-class_to_json.py`](8-class_to_json.py)
* Function that creates a class' dictionary corresponding to its JSON dump. Avoided module import.
### [`8-main.py`](8-main.py) & [`8-main_2.py`](8-main_2.py)
* **Tests:** `number` gets `89` or the `John` class calls the `win()` method
* Note: Sets or other non serializable object types will not be included in the class.

## 9-11. Student to JSON with filter/to disk and reload
### [`9-student.py`](9-student.py)
* Class with a method that returns the dictionary of the class. Avoided module import.
### [`10-student.py`](10-student.py)
* Added filter to only display a selection of attributes in the dictionary
### [`11-student.py`](11-student.py)
* Reloads a Student object instance with a dictionary
### [`9-main.py`](9-main.py) / [`10-main.py`](10-main.py) / [`11-main.py`](11-main.py)
* **Tests:**
    * John Doe, 23
    * Bob Dylan, 27
    * Fake Fake, 89
    * Call of all the instances to display their dictionaries

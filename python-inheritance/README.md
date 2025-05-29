# [Python - Inheritance](https://intranet.hbtn.io/projects/2127)

## 0. Lookup
### [`0-lookup.py`](0-lookup.py)
* Function that returns the list of available attributes and methods of an object. Avoided module import
### [`0-main.py`](0-main.py)
* **Tests:**
    * Lookup first empty class inheriting `object` class
    * Lookup second class with a method inheriting `object` class
    * Lookup `int` type

## 1. My list
### [`1-my_list.py`](1-my_list.py)
* Function that sorts and prints an instance of the new class `MyList` inheriting from `list`. Avoided module import
### [See test file](tests/inheritance.py)
* Note: all the elements of the list will be of type `int`

## 2. Exact same object
### [`2-is_same_class.py`](2-is_same_class.py)
* Function that checks whether an object is an instance of a class. Avoided module import
### [`2-main.py`](2-main.py)
* **Test:** `1` should be an `int`, but neither a `float` nor an `object`

## 3. Same class or inherit from
### [`3-is_kind_of_class.py`](3-is_kind_of_class.py)
* Function that checks whether an object is an instance or subclass of a class, or not. Avoided module import
### [`3-main.py`](3-main.py)
* **Test:** `1` should be an `int` and an `object`, but not a `float`

## 4. Only sub class of
### [`4-inherits_from.py`](4-inherits_from.py)
* Function that checks if is an instance of a subclass of a class. Avoided module import
### [`4-main.py`](4-main.py)
* **Test:** `1` should inherit from `int` and `object`, but not from `float`

## 5. Geometry module
### [`5-base_geometry.py`](5-base_geometry.py)
* Empty `BaseGeometry` class. Nothing to report. Avoided module import
### [`5-main.py`](5-main.py)
* Displays geometry info

## 6-11. BaseGeometry, Rectangle & Square classes
* `BaseGeometry` class with :
    * [`6-base_geometry.py`](6-base_geometry.py): an `area()` method
    * [`7-base_geometry.py`](7-base_geometry.py): an `integer_validator()` method **[(See test file)](tests/7-base_geometry.txt)**
    * [`8-rectangle.py`](8-rectangle.py): a `Rectangle` subclass
    * [`9-rectangle.py`](9-rectangle.py): a implementation of the `area()` super method
    * [`10-square.py`](10-square.py): a `Square` subclass
    * [`11-square.py`](11-square.py): a string description print method (`str()`)
    * Avoided module import.

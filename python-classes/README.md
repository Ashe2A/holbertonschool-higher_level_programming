# [Python - Classes and Objects](https://intranet.hbtn.io/projects/2124)

## 0. My first square
### [`0-square.py`](0-square.py)
* Empty `Square` class. Nothing to report. Avoided module import
### [`0-main.py`](0-main.py)
* Displays square info

## 1-6. Square class
* `Square` class with :
    * [`1-square.py`](1-square.py): a private `size` instance attribute
    * [`2-square.py`](2-square.py): as a positive integer (`TypeError` and `ValueError`).
    * [`3-square.py`](3-square.py): an `area` public method.
    * [`4-square.py`](4-square.py): a `size` getter and setter methods.
    * [`5-square.py`](5-square.py): a print method (`my_print()`).
    * [`6-square.py`](6-square.py): a `position` instance attribute, with getter and setter methods and updated print method (`my_print()`).
    * Avoided module import.

# Why a getter and setter?
`size` is a private attribute. It's to ensure control of the type and value. Getter and setter methods are not 100% Python, but more object-oriented programming. With them, validation of private attribute assignment is enabled, and how one gets the attribute value from the outside is defined (i.e. by assignment) Adding type/value validation in the setter will centralize the logic, since it ended up being done in only one place.

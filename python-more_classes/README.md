# [Python - Classes and Objects](https://intranet.hbtn.io/projects/2125)

## 0. Simple rectangle
### [`0-rectangle.py`](0-rectangle.py)
* Empty `Rectangle` class. Nothing to report. Avoided module import
### [`0-main.py`](0-main.py)
* Displays rectangle info

## 1-6. Rectangle class
* `Rectangle` class with :
    * [`1-rectangle.py`](1-rectangle.py): private `width` and `height` instance attributes with getters and setters (positive integers)
    * [`2-rectangle.py`](2-rectangle.py): `area()` and `perimeter()` instance methods
    * [`3-rectangle.py`](3-rectangle.py): `__str__()` and `print()` instance methods for string representation
    * [`4-rectangle.py`](4-rectangle.py): `__repr__()` method for object construction representation
    * [`5-rectangle.py`](5-rectangle.py): `__del__()` method for object deletion message
    * [`6-rectangle.py`](6-rectangle.py): class attribute `number_of_instances` in order to count the instances created
    * [`7-rectangle.py`](7-rectangle.py): class attribute `print_symbol` in order define which symbol for string representation
    * Avoided module import.

# Why a getter and setter?
`width` and `height` are private attributes. It's to ensure control of the types and values. Getter and setter methods are not 100% Python, but more object-oriented programming. With them, validation of private attribute assignment is enabled, and how one gets the attribute value from the outside is defined (i.e. by assignment) Adding type/value validation in the setter will centralize the logic, since it ended up being done in only one place.

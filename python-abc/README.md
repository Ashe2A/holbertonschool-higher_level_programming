# [Python - Abstract Classes and Interfaces](https://intranet.hbtn.io/projects/3104)

## 0. Abstract Animal Class and its Subclasses
### [`task_00_abc.py`](task_00_abc.py)
* Abstract `Animal` class as well as `Dog` and `Cat` subclasses.
### [`main_00_abc.py`](main_00_abc.py)
* **Tests:**
    * `Dog` sound: `'Bark'`
    * `Cat` sound: `'Meow'`

## 1. Shapes, Interfaces, and Duck Typing
### [`task_01_duck_typing.py`](task_01_duck_typing.py)
* Abstract `Shape` class as well as `Circle` and `Rectangle` subclasses.
### [`main_01_duck_typing.py`](main_01_duck_typing.py)
* **Tests:**
    * `Circle` of radius `5` has an area of `78.53981633974483` and a circumference `31.41592653589793`
    * `Rectangle` of width `4` and height `7` has an area of `28` and a perimeter `22`

## 2. Extending the Python List with Notifications
### [`task_02_verboselist.py`](task_02_verboselist.py)
* `VerboseList` class inheriting from `list` adding messages when a method is called.
### [`main_02_verboselist.py`](main_02_verboselist.py)
* **Tests:** with a the list `[1, 2, 3]`
    * `append(4)` should edit the list into `[1, 2, 3, 4]` and print `Added [4] to the list.`
    * `extend([5, 6])` should edit the list into `[1, 2, 3, 4, 5, 6]` and print `Extended the list with [2] items.`
    * `remove(2)` should print `Removed [2] from the list.` and edit the list into `[1, 3, 4, 5, 6]`
    * `pop()` should print `Popped [6] from the list.` and edit the list into `[1, 3, 4, 5]`
    * `pop(0)` should print `Popped [1] from the list.` and edit the list into `[3, 4, 5]`

## 2. Extending the Python List with Notifications
### [`task_02_verboselist.py`](task_02_verboselist.py)
* `VerboseList` class inheriting from `list` adding messages when a method is called.
### [`main_02_verboselist.py`](main_02_verboselist.py)
* **Tests:** with a the list `[1, 2, 3]`
    * `append(4)` should edit the list into `[1, 2, 3, 4]` and print `Added [4] to the list.`
    * `extend([5, 6])` should edit the list into `[1, 2, 3, 4, 5, 6]` and print `Extended the list with [2] items.`
    * `remove(2)` should print `Removed [2] from the list.` and edit the list into `[1, 3, 4, 5, 6]`
    * `pop()` should print `Popped [6] from the list.` and edit the list into `[1, 3, 4, 5]`
    * `pop(0)` should print `Popped [1] from the list.` and edit the list into `[3, 4, 5]`
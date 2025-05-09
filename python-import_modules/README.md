# [Python - import & modules](https://intranet.hbtn.io/projects/2175)

## 0. Import a simple function from a simple file
### [`0-add.py`](0-add.py)
* Adds two variable by importing the `add` function from [`add_0.py`](add_0.py), without importing wildcards. Avoided `__import__`-type import usage.
### [`0-import_add.py`](0-import_add.py)
* **Test:** Importing `0-add.py` shouldn't execute it.

## 1. My first toolbox!
### [`1-calculation.py`](1-calculation.py)
* Computes two variables by importing functions from [`calculator_1.py`](calculator_1.py) ans prints the math, without importing wildcards. Avoided `__import__`-type import usage. Importing `1-calculation.py` shouldn't execute it.
### [`calculator_1.py`](calculator_1.py)
* Contains math functions : `add` (addition), `sub` (substraction), `mul` (multiplication) and `div` (division).

## 2. How to make a script dynamic!
### [`2-args.py`](2-args.py)
* Prints all args and counts them. Importing `2-args.py` shouldn't execute it.

## 3. Infinite addition
### [`3-infinite_add.py`](3-infinite_add.py)
* Sums up all args and prints them. Importing `3-infinite_add.py` shouldn't execute it.
* Note : Only use this script with integer-castable numbers.
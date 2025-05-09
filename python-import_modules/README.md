# [Python - import & modules](https://intranet.hbtn.io/projects/2175)

## 0. Import a simple function from a simple file
### [`0-add.py`](0-add.py)
* Adds two variable by importing the `add` function from [`add_0.py`](add_0.py), without importing wildcards. Avoided `__import__`-type import usage.
### [`0-import_add.py`](0-import_add.py)
* **Test:** Importing `0-add.py` shouldn't execute the script.

## 1. My first toolbox!
### [`1-calculation.py`](1-calculation.py)
* Adds two variable by importing functions from [`calculator_1.py`](calculator_1.py), without importing wildcards. Avoided `__import__`-type import usage. Importing `1-calculation.py` shouldn't execute the script.
### [`calculator_1.py`](calculator_1.py)
* Contains math functions : `add` (addition), `sub` (substraction), `mul` (multiplication) and `div` (division).
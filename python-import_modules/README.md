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
* Prints all args and counts them. Importing the script shouldn't execute it.

## 3. Infinite addition
### [`3-infinite_add.py`](3-infinite_add.py)
* Sums up all args and prints them. Importing the script shouldn't execute it.
* Note : Only use this script with integer-castable numbers.

## 4. Who are you? <small>(for archive purposes)</small>
### [`4-hidden_discovery.py`](4-hidden_discovery.py)
* Lists all non-private (that don't start with two underscores `__`) name definitions in the [`hidden_4.pyc`](hidden_4.pyc) module, imported via the following curl command :
```
curl -Lso 'hidden_4.pyc' 'https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc'
```
* Importing `4-hidden_discovery.py` shouldn't execute it. This file needs to be used in a namespace folder, such as `/tmp/`.

## 5. Everything can be imported
### [`5-variable_load.py`](5-variable_load.py)
* Imports and prints the value of the `a` (with the value `98`) variable, contained in the [`variable_load_5.py`](variable_load_5.py), without importing wildcards. Avoided `__import__`-type import usage. Importing `5-variable_load.py` shouldn't execute it.

## 6. Build my own calculator!
### [`5-variable_load.py`](5-variable_load.py)
* Computes arguments like a calculator `a` (with the value `98`) variable, contained in the [`variable_load_5.py`](variable_load_5.py), without importing wildcards. Avoided `__import__`-type import usage. Importing `5-variable_load.py` shouldn't execute it.

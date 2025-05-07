# [Python - if/else, loops, functions](https://intranet.hbtn.io/projects/2172)

## 0. Positive anything is better than negative nothing
### [`0-positive_or_negative.py`](0-positive_or_negative.py)
* Randomizes the variable `number` and prints if it's negative, positive or zero, followed by a newline.

## 1. The last digit
### [`1-last_digit.py`](1-last_digit.py)
* Randomizes the variable `number` and prints if the last digit is between 0 and 5, greater than 5 or 0.

## 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
### [`2-print_alphabet.py`](2-print_alphabet.py)
* Prints lowercase alphabet, with one loop and neither imports nor storage.

## 3. When I was having that alphabet soup, I never thought that it would pay off
### [`3-print_alphabt.py`](3-print_alphabt.py)
* Prints lowercase alphabet except `q` and `e`, with one loop and neither imports nor variable storage.

## 4. Hexadecimal printing
### [`4-print_hexa.py`](4-print_hexa.py)
* Prints all numbers from `0` to `98` in decimal and in hexadecimal, with one loop and neither imports nor variable storage.

## 5. 00...99
### [`5-print_comb2.py`](5-print_comb2.py)
* Prints all numbers from `00` to `99` in decimal separated by a comma and followed by a newline. Uses no more than 2 prints with string format, with one loop and neither imports nor variable storage.

## 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
### [`6-print_comb3.py`](6-print_comb3.py)
* Prints all numbers from `01` to `89` in decimal separated by a comma and followed by a newline. Every number must have the first digit greater than the second. Uses no more than 3 `print` functions with string format, with 2 loops and neither imports nor variable storage.

## 7. islower
### [`7-islower.py`](7-islower.py)
* Function that returns whether a character is a lowercase letter without using `str.upper()` or `str.isupper()`, imports or modules.
### [`7-main.py`](7-main.py)
* **Tests:**
    * `a` (lowercase)
    * `H` (uppercase)
    * `A` (uppercase)
    * `3` (other)
    * `g` (lowercase).
    * Note: The main function prints uppercase even for non letter characters, due to only checking lowercase letters.

## 8. To uppercase
### [`8-uppercase.py`](8-uppercase.py)
* Function that turns lowercase letters of a string into uppercase ones, using 2 `print` functions with string format, one loop, and neither `str.upper()` or `str.isupper()`, imports nor modules.
### [`8-main.py`](8-main.py)
* **Tests:**
    * `"best"`: `"BEST"`
    * `"Best School 98 Battery street"`: `"BEST SCHOOL 98 BATTERY STREET"`

## 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
### [`9-print_last_digit.py`](9-print_last_digit.py)
* Function that prints the last digit of a number, without imports nor modules.
### [`9-main.py`](9-main.py)
* **Tests:**
    * `98`: Prints `"8"`
    * `0`: Prints `"0"`
    * `-1024`: Prints `"4"`
        * Returns `4`

## 10. a + b
### [`10-add.py`](10-add.py)
* Function that adds two integers, without imports nor modules.
### [`10-main.py`](10-main.py)
* **Tests:**
    * `1` + `2` = `3`
    * `98` + `0` = `98`
    * `100` + `-2` = `98`

## 11. a ^ b
### [`11-pow.py`](11-pow.py)
* Function that returns a number to the power of a second one, without imports nor modules.
### [`11-main.py`](11-main.py)
* **Tests:**
    * `2`<sup>`2`</sup> = `4`
    * `98`<sup>`2`</sup> = `9604`
    * `98`<sup>`0`</sup> = `1`
    * `100`<sup>`-2`</sup> = `0.0001`
    * `-4`<sup>`5`</sup> = `-1024`

## 12. Fizz Buzz
### [`12-fizzbuzz.py`](12-fizzbuzz.py)
* Function that lists all numbers from 1 to 100, replacing multiples of 3 with `Fizz` and those of 5 by `Buzz` (multiples of 15, combination of 5 and 3, are replaced by `FizzBuzz`).
### [`12-main.py`](12-main.py)
* **Tests:** The test will only call the `fizzbuzz` function, with a newline, as there is only one possible output :

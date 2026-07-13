# 0x02. Python - import & modules

## Description

This project covers how to import functions from other files, how to create
modules, and how to use command line arguments in Python. It is part of the
ALX Higher Level Programming curriculum.

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- Code uses the `pycodestyle` style (version 2.8.*)
- All files must be executable
- The length of files will be tested using `wc`

## Files

| File | Description |
| --- | --- |
| `0-add.py` | Imports the function `add` from `add_0.py` and prints the result of `1 + 2 = 3` |
| `0-import_add.py` | Imports the function `add(a, b)` from the file `add_0.py` |
| `1-calculation.py` | Imports functions from `calculator_1.py`, performs operations, and prints results |
| `2-args.py` | Prints the number of and the list of its command line arguments |
| `3-infinite_add.py` | Prints the result of the addition of all arguments |
| `4-hidden_discovery.py` | Prints all the names defined by the compiled module `hidden_4.pyc` |
| `5-variable_load.py` | Imports the variable `a` from `variable_load_5.py` and prints its value |
| `100-my_calculator.py` | Handles basic operations using imported functions from `calculator_1.py` |
| `101-easy_print.py` | Prints `#pythoniscool` without using `print` or `eval` or `open` or `import` |
| `102-magic_calculation.py` | Python function matching a given Python bytecode |
| `103-fast_alphabet.py` | Prints the alphabet in uppercase without loops or conditionals |
| `add_0.py` | Contains the `add(a, b)` function |
| `calculator_1.py` | Contains basic calculator functions: `add`, `sub`, `mul`, `div` |
| `magic_calculation_102.py` | Module used by `102-magic_calculation.py` |
| `variable_load_5.py` | Contains the variable `a` used by `5-variable_load.py` |

## Usage

Make sure all scripts are executable before running:

```bash
chmod +x *.py
```

### Examples

```bash
# Task 0 - import and use add function
$ ./0-import_add.py
1 + 2 = 3

# Task 2 - command line arguments
$ ./2-args.py
0 arguments.

$ ./2-args.py Hello Welcome To ALX
4 arguments:
1: Hello
2: Welcome
3: To
4: ALX

# Task 3 - infinite add
$ ./3-infinite_add.py 1 2 3 4 5
15

# Task 100 - calculator
$ ./100-my_calculator.py 10 + 5
10 + 5 = 15

$ ./100-my_calculator.py 10 / 0
Error: Division by zero

# Task 101 - easy print
$ ./101-easy_print.py
#pythoniscool

# Task 103 - fast alphabet
$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

## Author

Adamu Tajudeen Bawumia

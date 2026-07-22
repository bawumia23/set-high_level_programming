# 0x08. Python - More Classes and Objects

## Description

This project goes deeper into Object-Oriented Programming in Python,
building on the `Square` work from `python-classes`. It introduces the
Python "dunder" (double-underscore) methods that let a custom class hook
into built-in language behavior: `__str__`, `__repr__`, and `__del__`. It
also covers class attributes shared across every instance, static
methods, and class methods — and finishes with a classic algorithmic
challenge, the N Queens puzzle, solved with backtracking.

The core exercise builds a single `Rectangle` class incrementally across
ten tasks, each one adding a new capability on top of the last.

## Learning Objectives

- The difference between instance methods, class methods, and static
  methods, and when to use each
- How to dynamically add new attributes to an existing object
- What `__str__` and `__repr__` are and when each one is used
  (`print()`/`str()` call `__str__`; `repr()`, and the interactive
  interpreter's default display, call `__repr__`)
- Why `repr()` should be able to recreate an equivalent object via
  `eval()`
- What `__del__` is and when it runs (garbage collection / explicit
  `del`)
- How to control access to an attribute with getters and setters
  (properties), continuing from `python-classes`
- How class attributes (`number_of_instances`, `print_symbol`) are
  shared across every instance, unlike private instance attributes
- How to solve a constraint-satisfaction problem (N Queens) with
  backtracking

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5+
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Code follows the `pycodestyle` style guide (version 2.8.\*)
- All files must be executable
- All modules, classes, and functions/methods have documentation
- No module is allowed to import anything unless explicitly stated in
  the task (`101-nqueens.py` is only allowed to import `sys`)

## Files

| File | Description |
| --- | --- |
| `0-rectangle.py` | An empty `Rectangle` class |
| `1-rectangle.py` | `Rectangle` with `width`/`height` as validated private properties |
| `2-rectangle.py` | `Rectangle` adds `area()` and `perimeter()` |
| `3-rectangle.py` | `Rectangle` adds `__str__` (draws the rectangle with `#`) |
| `4-rectangle.py` | `Rectangle` adds `__repr__`, recreatable via `eval()` |
| `5-rectangle.py` | `Rectangle` adds `__del__`, printing `Bye rectangle...` on deletion |
| `6-rectangle.py` | `Rectangle` adds the class attribute `number_of_instances` |
| `7-rectangle.py` | `Rectangle` adds the class attribute `print_symbol`, used in `__str__` |
| `8-rectangle.py` | `Rectangle` adds the static method `bigger_or_equal()` |
| `9-rectangle.py` | `Rectangle` adds the class method `square()` |
| `101-nqueens.py` | Solves the N Queens puzzle via backtracking, printing every solution |

## Usage

Each task file can be imported and used independently, e.g.:

```
$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```

`101-nqueens.py` is run directly from the command line:

```
$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Author

Tajudeen — ALX Software Engineering, `set-high_level_programming` repo

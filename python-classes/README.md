# 0x06. Python - Classes and Objects

## Description

This project covers the fundamentals of Object-Oriented Programming in
Python: how to define a class, the difference between public, protected,
and private attributes, how properties (getters/setters) let you control
attribute access, and how to implement Python's "dunder" methods to make
custom objects behave like built-ins (printable, comparable, etc.).

The project builds a single `Square` class incrementally across several
tasks, each one adding a new capability on top of the last, followed by a
`Node` / `SinglyLinkedList` implementation and a reverse-engineering
exercise from Python bytecode.

## Learning Objectives

- What is OOP, and the difference between a class and an instance
- What is the difference between a public, protected, and private attribute
- How to define, use, and understand getters/setters (properties)
- Why Python is not a "pure" OOP language and how it handles name mangling
  (`__attr` → `_ClassName__attr`)
- How to use the `property` decorator
- How to dynamically create arbitrary new attributes on objects
- How to bind attributes to object types
- What is duck typing, and how it relates to Python's dynamic typing
- How to write class-level, instance-level, and static methods (in
  concept — used implicitly via the `@property` pattern here)
- How to implement comparison and string-representation dunder methods

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5+
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Code follows the `pycodestyle` style guide (version 2.8.\*)
- All files must be executable
- The length of files is tested using `wc`
- All modules, classes, and functions/methods have documentation
  (verified with `python3 -c 'print(__import__("module").__doc__)'`, etc.)
- No module is allowed to import anything unless explicitly stated in the
  task

## Files

| File | Description |
| --- | --- |
| `0-square.py` | An empty `Square` class |
| `1-square.py` | `Square` with a private instance attribute `size`, no validation |
| `2-square.py` | `Square` with `size` validated as an int `>= 0` |
| `3-square.py` | `Square` adds an `area()` method |
| `4-square.py` | `Square` exposes `size` through a property getter/setter |
| `5-square.py` | `Square` adds a `my_print()` method that draws the square with `#` |
| `6-square.py` | `Square` adds a `position` property so the square can be drawn offset on a grid |
| `100-singly_linked_list.py` | `Node` and `SinglyLinkedList` classes; `sorted_insert()` keeps the list in increasing order |
| `101-square.py` | `Square` becomes printable directly (`print(square)`) via `__str__`, matching `my_print()`'s output |
| `102-square.py` | `Square`'s `size` now accepts `int` or `float`; adds `==`, `!=`, `<`, `<=`, `>`, `>=` based on area |
| `103-magic_class.py` | `MagicClass`, a circle class reverse-engineered from a Python bytecode disassembly |

## Usage

Each task file can be imported and used independently, e.g.:

```
$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

$ ./4-main.py
Area: 7921 for size: 89
```

## Author

Tajudeen — ALX Software Engineering, `set-high_level_programming` repo

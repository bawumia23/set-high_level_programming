# 0x0A. Python - Inheritance

ALX Software Engineering - `set-high_level_programming` repository.

This project covers Python's inheritance model: introspecting objects
with `dir()`, distinguishing exact type matches from subclass
relationships (`type() is`, `isinstance()`), building a small
`BaseGeometry` -> `Rectangle` -> `Square` class hierarchy with shared
validation logic, and overriding dunder methods (`__eq__`, `__ne__`,
`__str__`) on subclasses of built-in types.

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-lookup.py` | Return the list of attributes/methods of an object |
| 1 | `1-my_list.py` | `MyList`, a `list` subclass with `print_sorted()` |
| 2 | `2-is_same_class.py` | Check if an object's type is exactly a given class |
| 3 | `3-is_kind_of_class.py` | Check if an object is an instance of a class or subclass |
| 4 | `4-inherits_from.py` | Check if an object's class is a strict subclass of another |
| 5 | `5-base_geometry.py` | Empty `BaseGeometry` class |
| 6 | `6-base_geometry.py` | Adds an `area()` that raises until overridden |
| 7 | `7-base_geometry.py` | Adds `integer_validator()` for positive-int checks |
| 8 | `8-rectangle.py` | `Rectangle`, with private validated `width`/`height` |
| 9 | `9-rectangle.py` | Adds `area()` and `__str__` to `Rectangle` |
| 10 | `10-square.py` | `Square` built on `Rectangle`, with private `size` |
| 11 | `11-square.py` | Adds a `[Square] <w>/<h>` `__str__` |
| 100 | `100-my_int.py` | `MyInt`, an `int` subclass with inverted `==`/`!=` |
| 101 | `101-add_attribute.py` | Add an attribute to an object, if possible (no try/except) |

## Testing

Most tasks have a matching `N-main.py`, taken directly from the spec:

```bash
./0-main.py
./1-main.py
# ... etc
```

Tasks 1 and 7 also have doctest files under `tests/`, run with:

```bash
python3 -m doctest ./tests/*
```

## Author

Tajudeen ([@bawumia23](https://github.com/bawumia23))

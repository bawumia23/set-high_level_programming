# 0x0B. Python - Almost a Circle (Part 1)

## Description
This project builds up a small OOP model in Python: a `Base` class that
manages a unique `id` for every object and provides shared JSON/CSV
serialization helpers, a `Rectangle` class that inherits from `Base`, and
a `Square` class that inherits from `Rectangle`.

By the end of the project, `Rectangle` and `Square` instances can be:
- validated on every attribute (`width`, `height`, `x`, `y`)
- displayed on stdout with `#`
- converted to/from a dictionary
- serialized to/from JSON (`save_to_file` / `load_from_file`)
- serialized to/from CSV (`save_to_file_csv` / `load_from_file_csv`)

## Environment
- Ubuntu 20.04 LTS
- python3 (version 3.8.5)
- pycodestyle (version 2.8.*)

## Files

| File | Description |
| --- | --- |
| `models/base.py` | `Base` class: id management, JSON/CSV helpers |
| `models/rectangle.py` | `Rectangle` class (inherits from `Base`) |
| `models/square.py` | `Square` class (inherits from `Rectangle`) |
| `tests/test_models/` | Unit tests, mirroring the `models/` structure |
| `N-main.py` | Example scripts demonstrating each task |

## Usage

Run the example scripts directly, e.g.:
```
./5-main.py
```

Run the full test suite:
```
python3 -m unittest discover tests
```

Run a single test file:
```
python3 -m unittest tests/test_models/test_rectangle.py
```

Check PEP 8 compliance:
```
pycodestyle models/*.py tests/test_models/*.py
```

## Author
Tajudeen ([@bawumia23](https://github.com/bawumia23)) — ALX Software
Engineering Program

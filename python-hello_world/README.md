# python-hello_world

An introductory project to Python scripting: running Python from shell
scripts, printing with `print()` and f-strings, string indexing and
slicing, standard streams, byte-compiling `.py` files, reading Python
bytecode, and a linked-list technical interview exercise in C.

## Requirements

* Ubuntu 20.04 LTS, `python3` (3.8.5)
* Style: `pycodestyle` 2.8.*
* All Python and Bash files are executable and start with the required
  shebang (`#!/usr/bin/python3` or `#!/bin/bash`)
* C files compiled with `gcc -Wall -Werror -Wextra -pedantic -std=gnu89`
  and written in Betty style

## Files

| File | Description |
| --- | --- |
| `0-run` | Shell script that runs the Python file named in `$PYFILE` |
| `1-run_inline` | Shell script that runs the Python code stored in `$PYCODE` |
| `2-print.py` | Prints a fixed string using `print()` |
| `3-print_number.py` | Prints an integer using an f-string |
| `4-print_float.py` | Prints a float with 2-digit precision using an f-string |
| `5-print_string.py` | Prints a string 3 times, then its first 9 characters |
| `6-concat.py` | Builds and prints a welcome message from two variables |
| `7-edges.py` | Extracts and prints the first 3, last 2, and middle characters of a word |
| `8-concat_edges.py` | Prints a phrase built purely from slicing an existing string |
| `9-easter_egg.py` | Prints the Zen of Python |
| `10-check_cycle.c`, `10-linked_lists.c`, `lists.h` | C: detects a cycle in a singly linked list (Floyd's algorithm) |
| `100-write.py` | Writes a message to stderr and exits with status 1 |
| `101-compile` | Shell script that compiles the Python file in `$PYFILE` to `$PYFILEc` |
| `102-magic_calculation.py` | Python function reconstructed from given bytecode |

## Author

Tajudeen

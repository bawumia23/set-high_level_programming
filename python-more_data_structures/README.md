# 0x04. Python - more_data_structures

ALX Software Engineering - `set-high_level_programming` repository.

This project covers Python dictionaries, sets, and further list/matrix
manipulation - including operations built with `map()` instead of loops -
plus a CPython C extension task that inspects `PyListObject` and
`PyBytesObject` internals directly.

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-square_matrix_simple.py` | Square every value in a matrix |
| 1 | `1-search_replace.py` | Replace all occurrences of an element in a list |
| 2 | `2-uniq_add.py` | Sum all unique integers in a list |
| 3 | `3-common_elements.py` | Return the common elements of two sets |
| 4 | `4-only_diff_elements.py` | Return elements present in only one set |
| 5 | `5-number_keys.py` | Return the number of keys in a dictionary |
| 6 | `6-print_sorted_dictionary.py` | Print a dictionary by ordered keys |
| 7 | `7-update_dictionary.py` | Replace or add a key/value pair |
| 8 | `8-simple_delete.py` | Delete a key from a dictionary |
| 9 | `9-multiply_by_2.py` | Return a new dict with all values x2 |
| 10 | `10-best_score.py` | Return the key with the highest value |
| 11 | `11-multiply_list_map.py` | Multiply list values by a number, using `map` |
| 12 | `12-roman_to_int.py` | Convert a Roman numeral to an integer |
| 100 | `100-weight_average.py` | Compute a weighted average of (score, weight) tuples |
| 101 | `101-square_matrix_map.py` | Square a matrix, using `map` (no loops) |
| 102 | `102-complex_delete.py` | Delete all keys matching a given value |
| 103 | `103-python.c` | C functions inspecting `PyListObject` / `PyBytesObject` |

## Testing

Each task has a matching `N-main.py` test file, taken directly from the
project spec.

```bash
./0-main.py
./1-main.py
# ... etc
```

For task 103, compile the shared library first:

```bash
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared \
    -Wl,-soname,libPython.so -o libPython.so -fPIC \
    -I/usr/include/python3.<minor> 103-python.c
python3 103-tests.py
```

Replace `<minor>` with your system's installed Python 3 minor version
(the original spec targeted 3.4; this was built and verified against 3.12,
since the relevant struct layouts have been stable since 3.4).

## Author

Tajudeen ([@bawumia23](https://github.com/bawumia23))

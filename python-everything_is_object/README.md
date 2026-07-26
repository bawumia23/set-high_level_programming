# 0x09. Python - everything is object

ALX Software Engineering - `set-high_level_programming` repository.

This project covers Python's object model: how variables are references
to objects, `id()`/`type()`, `is` vs `==`, mutability, integer/string
interning in CPython, and how mutable vs immutable arguments behave when
passed into functions.

## Tasks

Most tasks are short conceptual answers stored in `N-answer.txt` files
(no shebang needed - just the raw answer text). A few are short scripts:

| # | File | Description |
|---|------|-------------|
| 0 | `0-answer.txt` | Function to get an object's type |
| 1 | `1-answer.txt` | Function to get an object's identifier/address |
| 2-5 | `2-answer.txt` ... `5-answer.txt` | Same object or not, for ints |
| 6-13 | `6-answer.txt` ... `13-answer.txt` | `==` vs `is` for strings and lists |
| 14-18 | `14-answer.txt` ... `18-answer.txt` | Mutation vs rebinding, pass-by-reference |
| 19 | `19-copy_list.py` | Return a shallow copy of a list (max 3 lines) |
| 20-26 | `20-answer.txt` ... `26-answer.txt` | Tuple identity questions |
| 27-28 | `27-answer.txt`, `28-answer.txt` | List identity after `+` vs `+=` |
| 29/100 | `100-magic_string.py` | Stateful string builder using a mutable default arg (max 4 lines) |
| 30/101 | `101-locked_class.py` | Class restricting dynamic attribute creation |
| 31-34 | `103-*.txt`, `104-*.txt`, `105-line1.txt`, `106-*.txt` | CPython int/string object creation and small-int/string caching |

## Testing

```bash
./19-main.py
./100-main.py
./101-main.py
```

## Author

Tajudeen ([@bawumia23](https://github.com/bawumia23))

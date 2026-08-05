# Python - Input/Output

This project covers Python file I/O operations, JSON serialization/deserialization, and basic log parsing.

## Files

| File | Description |
|------|-------------|
| `0-read_file.py` | Reads a text file (UTF-8) and prints to stdout |
| `1-write_file.py` | Writes a string to a text file, returns chars written |
| `2-append_write.py` | Appends a string to a text file, returns chars added |
| `3-to_json_string.py` | Returns JSON string representation of an object |
| `4-from_json_string.py` | Returns Python object from a JSON string |
| `5-save_to_json_file.py` | Writes an object to a text file using JSON |
| `6-load_from_json_file.py` | Creates an object from a JSON file |
| `7-add_item.py` | Script: adds all CLI args to a list and saves to JSON |
| `8-class_to_json.py` | Converts class instance to JSON-serializable dict |
| `9-student.py` | `Student` class with `to_json()` method |
| `10-student.py` | `Student` class with filtered `to_json(attrs)` |
| `11-student.py` | `Student` class with `reload_from_json()` |
| `12-pascal_triangle.py` | Returns Pascal's triangle of `n` |
| `100-append_after.py` | Inserts text after lines containing a search string |
| `101-stats.py` | Reads stdin and computes HTTP log metrics |

## Requirements

- Python 3.8+
- No external modules (stdlib only, except `json` where allowed)
- All files executable where applicable

## Usage

```bash
# Test read_file
python3 -c "from read_file import read_file; read_file('my_file.txt')"

# Test Pascal's triangle
python3 -c "from pascal_triangle import pascal_triangle; print(pascal_triangle(5))"

# Test log parser
./101-generator.py | ./101-stats.py
```

## Author

[Your Name]

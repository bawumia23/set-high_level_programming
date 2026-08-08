# Python - Test-Driven Development

This project contains Python functions developed using test-driven development (TDD) principles. Each function is accompanied by doctest test cases.

## Files

### Task 0: Integers Addition
- `0-add_integer.py` - Function that adds two integers (or floats cast to int)
- `tests/0-add_integer.txt` - Doctest cases

### Task 1: Divide a Matrix
- `2-matrix_divided.py` - Function that divides all elements of a matrix by a number
- `tests/2-matrix_divided.txt` - Doctest cases

### Task 2: Say My Name
- `3-say_my_name.py` - Function that prints a formatted full name
- `tests/3-say_my_name.txt` - Doctest cases

### Task 3: Print Square
- `4-print_square.py` - Function that prints a square of '#' characters
- `tests/4-print_square.txt` - Doctest cases

### Task 4: Text Indentation
- `5-text_indentation.py` - Function that prints text with 2 new lines after `.`, `?`, `:`
- `tests/5-text_indentation.txt` - Doctest cases

### Task 5: Max Integer - Unittest
- `6-max_integer.py` - Function that finds the maximum integer in a list
- `tests/6-max_integer_test.py` - Unittest cases

### Task 6: Matrix Multiplication
- `100-matrix_mul.py` - Function that multiplies two matrices
- `tests/100-matrix_mul.txt` - Doctest cases

### Task 7: Lazy Matrix Multiplication
- `101-lazy_matrix_mul.py` - Function that multiplies two matrices using NumPy
- `tests/101-lazy_matrix_mul.txt` - Doctest cases

## Requirements

- Python 3.8.5
- pycodestyle 2.8.*
- NumPy 1.15.0 (for task 7)

## Running Tests

### Doctests
```bash
python3 -m doctest -v ./tests/0-add_integer.txt
python3 -m doctest -v ./tests/2-matrix_divided.txt
python3 -m doctest -v ./tests/3-say_my_name.txt
python3 -m doctest -v ./tests/4-print_square.txt
python3 -m doctest -v ./tests/5-text_indentation.txt
python3 -m doctest -v ./tests/100-matrix_mul.txt
python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt
```

### Unittests
```bash
python3 -m unittest tests.6-max_integer_test
```

## Author

This project is part of the Holberton School high-level programming curriculum.

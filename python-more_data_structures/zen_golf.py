"""
AI Refactoring: The Zen of Python

This module compares verbose, explicit programming styles with elegant,
Pythonic refactorings. It utilizes built-in functions, generator expressions,
and list comprehensions, referencing core principles of the Zen of Python.
"""


# =====================================================================
# Function 1: Sum of Even Numbers
# =====================================================================

def sum_even_verbose(numbers):
    """Sums all even numbers in a list using a traditional loop."""
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total


def sum_even_pythonic(numbers):
    """
    Sums all even numbers using a generator expression inside sum().

    Zen Principles Applied:
    - "Beautiful is better than ugly." (Replaces multi-line accumulation)
    - "Simple is better than complex." (Leverages built-in capabilities)
    """
    return sum(num for num in numbers if num % 2 == 0)


# =====================================================================
# Function 2: Find the Longest Word
# =====================================================================

def longest_word_verbose(words):
    """Finds the longest word in a list using a traditional loop."""
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def longest_word_pythonic(words):
    """
    Finds the longest word using the built-in max() function with a key.

    Zen Principles Applied:
    - "Flat is better than nested." (Removes the nested loop-if block)
    - "Readability counts." (The intent 'max by length' is instantly clear)
    """
    if not words:
        return ""
    return max(words, key=len)


# =====================================================================
# Function 3: Filter Positive Numbers
# =====================================================================

def filter_positive_verbose(numbers):
    """Filters positive numbers into a new list using an explicit loop."""
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


def filter_positive_pythonic(numbers):
    """
    Filters positive numbers using a declarative list comprehension.

    Zen Principles Applied:
    - "Beautiful is better than ugly."
    - "Sparse is better than dense." (Clean, expressive single-line pipeline)
    """
    return [num for num in numbers if num > 0]


# =====================================================================
# Measurement & Verification Suite
# =====================================================================

def count_characters(code):
    """Calculates character count excluding whitespace and newlines."""
    return len(code.replace(" ", "").replace("\n", ""))


def avg_line_length(code):
    """Calculates the average length of non-empty lines."""
    lines = [line for line in code.split("\n") if line.strip()]
    return sum(len(line) for line in lines) / len(lines) if lines else 0


def test_equivalence():
    """Verifies that verbose and pythonic functions return identical results."""
    test_cases = [
        ([1, 2, 3, 4, 5, 6], "sum_even"),
        (["cat", "elephant", "dog", "whale"], "longest"),
        ([-3, -1, 0, 2, 5, -7], "filter_positive"),
    ]

    print("--- Running Equivalence Tests ---")

    # Test Case 1: Sum Even
    v1 = sum_even_verbose(test_cases[0][0])
    p1 = sum_even_pythonic(test_cases[0][0])
    assert v1 == p1, f"Mismatch: Verbose {v1} != Pythonic {p1}"
    print(f"Sum Even Test: PASSED (Result: {v1})")

    # Test Case 2: Longest Word
    v2 = longest_word_verbose(test_cases[1][0])
    p2 = longest_word_pythonic(test_cases[1][0])
    assert v2 == p2, f"Mismatch: Verbose {v2} != Pythonic {p2}"
    print(f"Longest Word Test: PASSED (Result: '{v2}')")

    # Test Case 3: Filter Positive
    v3 = filter_positive_verbose(test_cases[2][0])
    p3 = filter_positive_pythonic(test_cases[2][0])
    assert v3 == p3, f"Mismatch: Verbose {v3} != Pythonic {p3}"
    print(f"Filter Positive Test: PASSED (Result: {v3})")
    print("All tests passed successfully!\n")


if __name__ == "__main__":
    test_equivalence()
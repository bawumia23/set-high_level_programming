#!/usr/bin/python3
"""Prints all the names defined by the compiled module hidden_4.pyc."""
import importlib

if __name__ == "__main__":
    hidden_4 = importlib.import_module("hidden_4")
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    for name in sorted(names):
        print(name)

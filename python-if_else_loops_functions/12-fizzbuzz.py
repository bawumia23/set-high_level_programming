#!/usr/bin/python3
"""Module for the FizzBuzz game."""


def fizzbuzz():
    """Print numbers 1 to 100, replacing multiples of 3 and 5.

    Multiples of 3 print "Fizz", multiples of 5 print "Buzz",
    multiples of both print "FizzBuzz". Each followed by a space.
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

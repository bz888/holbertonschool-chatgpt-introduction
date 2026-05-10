#!/usr/bin/python3
"""
A simple recursive factorial program.

This script takes one command-line argument, converts it to an integer,
calculates its factorial recursively, and prints the result.

Usage:
    ./factorial_recursive.py 5

Output:
    120
"""

import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.

    Example:
        factorial(5) returns 120 because:
        5 * 4 * 3 * 2 * 1 = 120
    """
    if n == 0:
        return 1

    return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
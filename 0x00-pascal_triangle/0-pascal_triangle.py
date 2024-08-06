#!/usr/bin/python3
"""
pascal triangle algo
"""


def pascal_triangle(n):
    """
    Create and returns a list of integers
    that representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    triangle = pascal_triangle(n - 1)
    last_row = triangle[-1]
    new_row = [1]
    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])
    new_row.append(1)
    triangle.append(new_row)
    return triangle

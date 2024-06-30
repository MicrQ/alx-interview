#!/usr/bin/python3
""" pascal triangle implementation """


def pascal_triangle(n):
    """
        returns a list of lists of integers representing
        the Pascal triangle of n
    """
    triangle = [[1], [1, 1]]

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return triangle

    for i in range(2, n):
        j = 1
        prev = triangle[-1]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j] + prev[j - 1])
        row.append(1)
        triangle.append(row)
    return triangle

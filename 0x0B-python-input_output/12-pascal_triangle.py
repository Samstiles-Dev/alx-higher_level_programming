#!/usr/bin/python3
"""
  Mod that calculates pascal's _triangle
"""


def pascal_triangle(n):
    """
      Func that calculates pascal's _triangle
    """
    if n <= 0:
        return []

    _triangle = []
    for i in range(n):
        if i == 0:
            _triangle.append([1])
        else:
            row = [1]
            for j in range(i-1):
                row.append(_triangle[i-1][j] + _triangle[i-1][j+1])
            row.append(1)
            _triangle.append(row)
    return _triangle

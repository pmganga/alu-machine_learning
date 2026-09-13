#!/usr/bin/env python3
"""Module that returns the transpose of a 2D matrix."""


def matrix_transpose(matrix):
    """Computes the transpose of a 2D matrix.

    Args:
        matrix: A 2D list of numbers.

    Returns:
        A new 2D list representing the transposed matrix.
    """
    transposed = []
    num_cols = len(matrix[0])
    for j in range(num_cols):
        new_row = [matrix[i][j] for i in range(len(matrix))]
        transposed.append(new_row)
    return transposed

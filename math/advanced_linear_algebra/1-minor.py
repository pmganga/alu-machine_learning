#!/usr/bin/env python3
"""Module to calculate the minor matrix."""


def determinant(matrix):
    """Helper function to calculate the determinant."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(n):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    return det


def minor(matrix):
    """Calculates the minor matrix of a matrix."""
    if type(matrix) is not list or not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    minor_mat = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            sub_matrix = [row[:j] + row[j+1:] for r_idx, row in enumerate(matrix) if r_idx != i]
            minor_row.append(determinant(sub_matrix))
        minor_mat.append(minor_row)

    return minor_mat

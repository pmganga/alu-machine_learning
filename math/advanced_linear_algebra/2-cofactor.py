#!/usr/bin/env python3
"""Module to calculate the cofactor matrix."""


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


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix."""
    if type(matrix) is not list or not all(
            type(row) is list for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    cofactor_mat = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            sub_matrix = [
                row[:j] + row[j+1:]
                for r_idx, row in enumerate(matrix)
                if r_idx != i
            ]
            minor_val = determinant(sub_matrix)
            cofactor_row.append(minor_val * ((-1) ** (i + j)))
        cofactor_mat.append(cofactor_row)

    return cofactor_mat

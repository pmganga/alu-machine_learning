#!/usr/bin/env python3
"""Module that performs matrix multiplication on 2D matrices."""


def mat_mul(mat1, mat2):
    """Multiplies two 2D matrices.

    Args:
        mat1: First 2D matrix (m x k).
        mat2: Second 2D matrix (k x n).

    Returns:
        A new 2D matrix (m x n), or None if dimensions cannot multiply.
    """
    if len(mat1[0]) != len(mat2):
        return None

    rows1 = len(mat1)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = sum(mat1[i][k] * mat2[k][j] for k in range(cols1))
            row.append(total)
        result.append(row)
    return result

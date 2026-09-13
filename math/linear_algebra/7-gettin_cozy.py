#!/usr/bin/env python3
"""Module that concatenates two 2D matrices along a specific axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along axis 0 or 1.

    Args:
        mat1: First 2D matrix.
        mat2: Second 2D matrix.
        axis: 0 for vertical concatenation, 1 for horizontal concatenation.

    Returns:
        A new 2D matrix, or None if dimensions are incompatible.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]

    return None

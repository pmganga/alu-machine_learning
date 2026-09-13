#!/usr/bin/env python3
"""Module that adds two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise.

    Args:
        mat1: First 2D list of ints/floats.
        mat2: Second 2D list of ints/floats.

    Returns:
        A new 2D list with the element-wise sum, or None if shapes differ.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    new_mat = []
    for i in range(len(mat1)):
        row = [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
        new_mat.append(row)
    return new_mat

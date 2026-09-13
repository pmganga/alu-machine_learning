#!/usr/bin/env python3
"""Module that concatenates two matrices along a specific axis using numpy."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along a specified axis.

    Args:
        mat1: First numpy.ndarray.
        mat2: Second numpy.ndarray.
        axis: The axis along which arrays are joined.

    Returns:
        A new concatenated numpy.ndarray.
    """
    return np.concatenate((mat1, mat2), axis=axis)

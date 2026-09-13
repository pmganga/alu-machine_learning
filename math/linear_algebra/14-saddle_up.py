#!/usr/bin/env python3
"""Module that performs matrix multiplication using numpy."""
import numpy as np


def np_matmul(mat1, mat2):
    """Performs matrix multiplication.

    Args:
        mat1: First numpy.ndarray.
        mat2: Second numpy.ndarray.

    Returns:
        A new numpy.ndarray representing the matrix product.
    """
    return np.matmul(mat1, mat2)

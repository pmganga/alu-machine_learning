#!/usr/bin/env python3
"""Module that performs element-wise operations on numpy ndarrays."""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction, multiplication, division.

    Args:
        mat1: First numpy.ndarray.
        mat2: Second numpy.ndarray or scalar.

    Returns:
        A tuple of (sum, difference, product, quotient).
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

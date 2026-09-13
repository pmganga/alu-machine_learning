#!/usr/bin/env python3
"""Module that transposes a numpy ndarray."""


def np_transpose(matrix):
    """Transposes a numpy ndarray.

    Args:
        matrix: A numpy.ndarray.

    Returns:
        A new transposed numpy.ndarray.
    """
    return matrix.transpose()
    
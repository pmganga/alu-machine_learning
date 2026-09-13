#!/usr/bin/env python3
"""Module that transposes a numpy ndarray."""
import numpy as np


def np_transpose(matrix):
    """Transposes a numpy ndarray.

    Args:
        matrix: A numpy.ndarray or array-like object.

    Returns:
        A new transposed numpy.ndarray.
    """
    return np.transpose(matrix)

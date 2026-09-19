#!/usr/bin/env python3
"""Module to calculate the definiteness of a matrix."""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a numpy matrix."""
    if type(matrix) is not np.ndarray:
        raise TypeError("matrix must be a numpy.ndarray")

    if (len(matrix.shape) != 2 or
            matrix.shape[0] != matrix.shape[1] or
            matrix.shape[0] == 0):
        return None

    if not np.array_equal(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    if np.all(eigenvalues < 0):
        return "Negative definite"
    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"

    return "Indefinite"

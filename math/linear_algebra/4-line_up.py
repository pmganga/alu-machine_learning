#!/usr/bin/env python3
"""Module that adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Adds two 1D arrays element-wise.

    Args:
        arr1: List of ints/floats.
        arr2: List of ints/floats.

    Returns:
        A new list with the element-wise sum, or None if shapes differ.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]

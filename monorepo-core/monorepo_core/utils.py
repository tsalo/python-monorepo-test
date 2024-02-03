"""Utility functions for the monorepo package."""

import numpy as np


def sum_of_squares(a):
    """Calculate the sum of squares of ``a``."""
    a = np.asarray(a)
    return np.sum(a**2)

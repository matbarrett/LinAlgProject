"""Small SVD helpers used in the project notebooks."""

import numpy as np


def rank_k_approx(A, k):
    """Return a rank-at-most-k approximation, without clipping pixel values."""
    A = np.asarray(A, dtype=float)
    if A.ndim != 2:
        raise ValueError("A must be a two-dimensional matrix")
    if not isinstance(k, (int, np.integer)) or not 0 <= k <= min(A.shape):
        raise ValueError("k must be an integer from 0 to min(A.shape)")
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    return (U[:, :k] * s[:k]) @ Vt[:k, :]


def storage(m, n, k):
    """Count the numbers in the truncated U, s, and Vt factors."""
    return k * (m + n + 1)


def compression_ratio(m, n, k):
    """Compare number of original pixels with number of stored factor entries."""
    return (m * n) / storage(m, n, k)


def rel_error(A, B):
    """Relative Frobenius error, calculated using floating-point arithmetic."""
    A, B = np.asarray(A, dtype=float), np.asarray(B, dtype=float)
    norm = np.linalg.norm(A)
    if norm == 0:
        raise ValueError("Relative error is undefined for an all-zero original")
    return np.linalg.norm(A - B) / norm


def predicted_error(s, k):
    """Relative error from the discarded singular values of a nonzero matrix."""
    s = np.asarray(s, dtype=float)
    if not isinstance(k, (int, np.integer)) or not 0 <= k <= len(s):
        raise ValueError("k must be an integer from 0 to len(s)")
    total = np.sum(s**2)
    if total == 0:
        raise ValueError("Relative error is undefined for an all-zero original")
    return np.sqrt(np.sum(s[k:]**2) / total)

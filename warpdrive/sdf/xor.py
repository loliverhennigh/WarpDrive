"""SDF set operation: symmetric difference (exclusive OR).

Implements IQ formula:
    ``max(min(d1, d2), -max(d1, d2))``
"""

from __future__ import annotations

import sympy as sp

__all__ = ["xor"]


def xor(d1: sp.Expr, d2: sp.Expr) -> sp.Expr:
    """Return XOR (symmetric difference) distance field.

    Args:
        d1: First SDF.
        d2: Second SDF.
    """

    return sp.Max(sp.Min(d1, d2), -sp.Max(d1, d2)) 
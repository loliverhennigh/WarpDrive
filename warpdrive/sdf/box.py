"""Axis-aligned box signed-distance expression.

Given half-extents *b = (hx, hy, hz)* the distance formula follows
Inigo Quilez’ reference implementation:
https://www.youtube.com/watch?v=62-pRVZuS5c

.. math::
    q = |p| - b\\
    d = \|\max(q, 0)\|_2 + \min(\max(q_x, \max(q_y, q_z)), 0)

The function below returns the exact SymPy expression *d(x, y, z)*.
"""

from __future__ import annotations

import sympy as sp

from .symbols import x, y, z

__all__ = ["box"]


def box(half_extents: tuple[float, float, float]):
    """Signed-distance from an axis-aligned box centred at the origin.

    Args:
        half_extents: Tuple ``(hx, hy, hz)`` giving the positive half-length
            of the box along each axis.

    Returns:
        sympy.Expr: Distance expression ``d(x, y, z)``.
    """

    hx, hy, hz = map(float, half_extents)

    qx = sp.Abs(x) - hx
    qy = sp.Abs(y) - hy
    qz = sp.Abs(z) - hz

    outside = sp.sqrt(sp.Max(qx, 0) ** 2 + sp.Max(qy, 0) ** 2 + sp.Max(qz, 0) ** 2)
    inside = sp.Min(sp.Max(qx, sp.Max(qy, qz)), 0)
    return outside + inside 
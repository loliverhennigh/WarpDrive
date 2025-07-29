"""Cylinder signed-distance function utility."""

from __future__ import annotations

import sympy as sp

from .symbols import x, y, z

__all__ = ["cylinder"]


def cylinder(
    radius: float,
    height: float | None = None,
):
    """Return SDF for a cylinder aligned with the *z* axis.

    Parameters
    ----------
    radius
        Cylinder radius.
    height
        Total height. If *None*, produce an infinite cylinder.
    """

    expr_radial = sp.sqrt(x**2 + y**2) - float(radius)

    if height is None:
        expr = expr_radial
    else:
        half_h = float(height) / 2.0
        dz = sp.Abs(z) - half_h
        outside = sp.sqrt(sp.Max(expr_radial, 0) ** 2 + sp.Max(dz, 0) ** 2)
        expr = outside + sp.Min(sp.Max(expr_radial, dz), 0)

    return expr
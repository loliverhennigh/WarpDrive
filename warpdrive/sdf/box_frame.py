"""Signed-distance to a hollow *box frame* (axis-aligned).

This reproduces Inigo Quilez' exact formula (see ShaderToy `3ljcRh`). The
frame is obtained by subtracting a smaller box from a larger one, with a
uniform wall thickness `e`.
"""

from __future__ import annotations

import sympy as sp

from .symbols import x, y, z

__all__ = ["box_frame"]


def box_frame(half_extents: tuple[float, float, float], thickness: float):
    """Signed-distance to an axis-aligned box frame.

    Args:
        half_extents: Tuple ``(hx, hy, hz)`` of outer half-size.
        thickness: Frame wall thickness ``e`` (> 0).

    Returns:
        sympy.Expr: Expression ``d(x, y, z)``.
    """

    hx, hy, hz = map(float, half_extents)
    e = float(thickness)

    # p = abs(p) - b
    px = sp.Abs(x) - hx
    py = sp.Abs(y) - hy
    pz = sp.Abs(z) - hz

    # q = abs(p + e) - e
    qx = sp.Abs(px + e) - e
    qy = sp.Abs(py + e) - e
    qz = sp.Abs(pz + e) - e

    # Helper to build distance for a given orientation
    def d(px_, py_, pz_, qx_, qy_, qz_):
        outside_vec = sp.Matrix([
            sp.Max(px_, 0),
            sp.Max(py_, 0),
            sp.Max(pz_, 0),
        ])
        outside = sp.sqrt(outside_vec.dot(outside_vec))
        inside = sp.Min(sp.Max(px_, sp.Max(py_, pz_)), 0)
        return outside + inside

    d1 = d(px, qy, qz, None, None, None)
    d2 = d(qx, py, qz, None, None, None)
    d3 = d(qx, qy, pz, None, None, None)

    return sp.Min(d1, sp.Min(d2, d3)) 
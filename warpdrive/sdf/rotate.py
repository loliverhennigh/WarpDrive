"""Utility to rotate a signed-distance expression.

Given an original distance field *d(x, y, z)* we obtain the rotated field
by evaluating *d* in the *inverse-rotated* coordinates.  We support simple
Euler-angle rotations about the *x*, *y*, and *z* axes (radians).

Convention: rota = (rx, ry, rz) applies *Rx* then *Ry* then *Rz*
( intrinsic ZYX order, same as many graphics conventions ).
"""

from __future__ import annotations

import math

import sympy as sp

from .symbols import x, y, z

__all__ = ["rotate"]


Matrix = sp.Matrix  # alias for brevity


def _rotation_matrix(rx: float, ry: float, rz: float) -> Matrix:
    cx, sx = math.cos(rx), math.sin(rx)
    cy, sy = math.cos(ry), math.sin(ry)
    cz, sz = math.cos(rz), math.sin(rz)

    Rx = Matrix([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    Ry = Matrix([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    Rz = Matrix([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    # Apply Rx first, then Ry, then Rz: R = Rz * Ry * Rx
    return Rz * Ry * Rx


def rotate(expr: sp.Expr, angles: tuple[float, float, float]):
    """Rotate an SDF by Euler angles.

    Args:
        expr: SymPy SDF expression ``d(x, y, z)``.
        angles: Tuple ``(rx, ry, rz)`` in **radians** – rotations around the
            *x*, *y*, and *z* axes applied in that order.

    Returns:
        sympy.Expr: Rotated distance expression.
    """

    rx, ry, rz = angles
    R = _rotation_matrix(rx, ry, rz)

    # Inverse rotation for coordinates (R is orthonormal → R.T = R^{-1})
    Rt = R.T
    px, py, pz = Rt * Matrix([x, y, z])  # type: ignore[misc]

    subs_map = {x: px, y: py, z: pz}
    return expr.xreplace(subs_map) 
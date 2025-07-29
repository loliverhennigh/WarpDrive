"""Quick 3-D visualisation of signed-distance fields.

Usage example
-------------
>>> from warpdrive.sdf import sphere, plot_sdf
>>> plot_sdf(sphere(1.0), bbox=((-1.5, 1.5),) * 3, resolution=60)
"""

from __future__ import annotations

# ruff: noqa: F401
from typing import Tuple, Sequence, Union

import numpy as np
import sympy as sp

from .symbols import x, y, z
from .marching_cubes import sdf_to_mesh
from ..utils.package_management import require_package

__all__ = ["plot_sdf"]


ColorType = Union[str, Tuple[float, float, float], Tuple[float, float, float, float]]


def plot_sdf(
    expr: Union[sp.Expr, Sequence[sp.Expr]],
    *,
    bbox: Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]] = ((-1, 1), (-1, 1), (-1, 1)),
    resolution: int = 50,
    isolevel: float = 0.0,
    color: Union[ColorType, Sequence[ColorType]] = "cyan",
):
    """Render one or many SDFs.

    Parameters
    ----------
    expr : Expr or list[Expr]
        One expression or a list to visualise multiple solids.
    color : str or RGB/RGBA tuple or list
        Color specification(s). If *expr* is a list, *color* can be a list of
        equal length; otherwise a single value is used for all.
    Other parameters are forwarded to the sampler.
    """

    # normalise to list
    exprs = list(expr if isinstance(expr, (list, tuple)) else [expr])

    if isinstance(color, (list, tuple)) and len(color) != len(exprs):
        raise ValueError("Length of color list must match number of expressions")

    colors: Sequence[ColorType]
    if isinstance(color, (list, tuple)) and isinstance(color[0], (str, tuple)):
        colors = color  # type: ignore[assignment]
    else:
        colors = [color] * len(exprs)  # type: ignore[list-item]

    require_package("matplotlib")
    import matplotlib.pyplot as plt  # noqa: WPS433
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: WPS433

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")

    for expr_i, col in zip(exprs, colors):
        verts, faces = sdf_to_mesh(expr_i, bbox, resolution, isolevel=isolevel)
        mesh = Poly3DCollection(verts[faces], alpha=0.7, facecolor=col)
        ax.add_collection3d(mesh)

    (xmin, xmax), (ymin, ymax), (zmin, zmax) = bbox
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin, zmax)
    ax.set_box_aspect([xmax - xmin, ymax - ymin, zmax - zmin])
    plt.tight_layout()
    plt.show() 
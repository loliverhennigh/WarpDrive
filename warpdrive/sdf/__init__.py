"""
Signed Distance Function (SDF) utilities for 3-D geometry.

This subpackage builds symbolic SDFs using SymPy and offers
numeric evaluation helpers.
"""
from .sphere import sphere
from .cylinder import cylinder
from .box import box
from .round_box import round_box
from .box_frame import box_frame
from .union import union
from .subtraction import subtraction
from .intersection import intersection
from .xor import xor
from .translate import translate
from .rotate import rotate
from .difference import difference
# Optional plotting helper (slow import)
from .plotting import plot_sdf
from .symbols import x, y, z

__all__ = [
    "sphere",
    "cylinder",
    "box",
    "round_box",
    "box_frame",
    "union",
    "subtraction",
    "intersection",
    "xor",
    "translate",
    "rotate",
    "difference",
    "plot_sdf",
    "x",
    "y",
    "z",
] 
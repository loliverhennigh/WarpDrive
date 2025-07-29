import math
import sympy as sp

from warpdrive.sdf import sphere, rotate

x, y, z = sp.symbols("x y z")


def test_rotate_z90_equiv():
    s = sphere(1.0)
    s_rot = rotate(s, (0.0, 0.0, math.pi / 2))  # 90° around Z

    # Point (1,0,0) on surface maps to (0,1,0)
    val_orig = s.subs({x: 0, y: 1, z: 0})
    val_rot = s_rot.subs({x: 1, y: 0, z: 0})
    assert val_orig == val_rot == 0


def test_rotate_identity():
    s = sphere(1.0)
    s_rot = rotate(s, (0.0, 0.0, 0.0))
    assert sp.simplify(s - s_rot) == 0 
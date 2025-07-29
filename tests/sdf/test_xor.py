import sympy as sp

from warpdrive.sdf import sphere, box, xor

x, y, z = sp.symbols("x y z")


def test_xor_inside_one():
    s = sphere(1.0)
    b = box((0.5, 0.5, 0.5))
    xexpr = xor(s, b)
    val = xexpr.subs({x: 0.8, y: 0, z: 0})  # inside sphere only
    assert val < 0


def test_xor_inside_both():
    s = sphere(1.0)
    b = box((0.5, 0.5, 0.5))
    xexpr = xor(s, b)
    val = xexpr.subs({x: 0, y: 0, z: 0})  # inside both
    assert val > 0 
import sympy as sp

from warpdrive.sdf import sphere, box, subtraction

x, y, z = sp.symbols("x y z")


def test_subtraction_difference():
    s = sphere(1.0)
    b = box((0.5, 0.5, 0.5))
    d = subtraction(s, b)
    # Origin inside both -> positive (outside ring)
    val_origin = d.subs({x: 0, y: 0, z: 0})
    assert val_origin > 0

    # Point inside sphere only should be negative (inside A\B)
    val = d.subs({x: 0.8, y: 0, z: 0})
    assert val < 0 
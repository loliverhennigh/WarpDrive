import sympy as sp

from warpdrive.sdf import sphere, box, intersection

x, y, z = sp.symbols("x y z")


def test_intersection_max_property():
    s = sphere(1.0)
    b = box((0.5, 0.5, 0.5))
    i = intersection(s, b)
    subs = {x: 0, y: 0, z: 0}
    assert i.subs(subs) == sp.Max(s.subs(subs), b.subs(subs))


def test_intersection_outside_one():
    s = sphere(1.0)
    b = box((0.5, 0.5, 0.5))
    i = intersection(s, b)
    val = i.subs({x: 0.9, y: 0, z: 0})  # inside sphere only
    assert val > 0 
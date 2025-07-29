import sympy as sp

from warpdrive.sdf import sphere, box, union

x, y, z = sp.symbols("x y z")


def test_union_min_property():
    s = sphere(1.0)
    b = box((0.5, 0.5, 0.5))
    u = union(s, b)

    subs = {x: 0.9, y: 0, z: 0}
    val_s = s.subs(subs)
    val_b = b.subs(subs)
    val_u = u.subs(subs)
    assert val_u == sp.Min(val_s, val_b)


def test_union_outside():
    s = sphere(1.0)
    b = box((0.5, 0.5, 0.5))
    u = union(s, b)
    val = u.subs({x: 2, y: 0, z: 0})
    assert val > 0 
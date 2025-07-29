import sympy as sp

from warpdrive.sdf import sphere, translate

x, y, z = sp.symbols("x y z")


def test_translate_center():
    base = sphere(1.0)
    moved = translate(base, (1.0, 0.0, 0.0))
    # New center at (1,0,0) should give -1
    val = moved.subs({x: 1, y: 0, z: 0})
    assert val == sp.Float(-1)


def test_translate_original_outside():
    base = sphere(1.0)
    moved = translate(base, (1.0, 0.0, 0.0))
    val = moved.subs({x: 0, y: 0, z: 0})  # now should be outside, distance 0? Actually should be 0? distance -? center shift by 1 means point (0,0,0) at distance 1 inside? outside maybe positive 0? It is exactly 0 since radius1? Wait sphere radius1 center (1,0,0) point (0,0,0) is distance 1 => 0 surface.
    assert val == 0 
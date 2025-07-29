import pytest
import sympy as sp

pytest.importorskip("skimage")

from warpdrive.sdf import sphere
from warpdrive.sdf.marching_cubes import sdf_to_mesh

x, y, z = sp.symbols("x y z")


def test_sdf_to_mesh_basic():
    expr = sphere(1.0)
    verts, faces = sdf_to_mesh(expr, bbox=((-1.2, 1.2),) * 3, resolution=50)
    # Expect some vertices and faces
    assert verts.shape[1] == 3
    assert faces.shape[1] == 3
    assert len(verts) > 0 and len(faces) > 0 
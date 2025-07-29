"""Example: build and plot a circular RLC geometry."""

from warpdrive.geometry.circuit import CircularRLC

if __name__ == "__main__":
    geom = CircularRLC(coil_radius=1e-3)
    # coarse preview bbox inferred around origin
    geom.plot(bbox=((-0.002, 0.002),)*3, resolution=120) 
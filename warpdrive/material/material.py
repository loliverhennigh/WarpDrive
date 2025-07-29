"""Physical and material constants shared across WarpDrive.

Numbers are in SI units.
"""

from dataclasses import dataclass
from typing import Union, Tuple
from sympy import Expr

__all__ = ["Material", "VACUUM", "COPPER", "QUARTZ"]

# Material class
@dataclass(frozen=True)
class Material:
    name: str
    color: Tuple[float, float, float, float] = (255, 255, 255, 255) # RGBA
    permittivity: Union[float, Expr] = 8.854e-12  # F/m
    permeability: Union[float, Expr] = 4.0 * 3.14159e-7  # H/m
    electrical_conductivity: Union[float, Expr] = 0.0
    magnetic_conductivity: Union[float, Expr] = 0.0
    initial_electric_field: Union[Tuple[float, float, float], None] = None # E_x, E_y, E_z
    initial_magnetic_field: Union[Tuple[float, float, float], None] = None # B_x, B_y, B_z
    specific_heat: float = 100.0 # J/kg/K

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


VACUUM = Material(
    name="Vacuum",
    color=(255, 255, 255, 255),
    permittivity=8.854e-12,
    permeability=4.0 * 3.14159e-7,
    electrical_conductivity=0.0,
    magnetic_conductivity=0.0,
    specific_heat=0.0,
)
COPPER = Material(
    name="Copper",
    color=(255, 165, 0, 255),
    permittivity=8.854e-12,
    permeability=4.0 * 3.14159e-7,
    electrical_conductivity=5.96e7,
    magnetic_conductivity=0.0,
    specific_heat=385.0,
)
QUARTZ = Material(
    name="Quartz",
    color=(128, 128, 128, 16),
    permittivity=8.854e-12 * 3.9,
    permeability=4.0 * 3.14159e-7,
    electrical_conductivity=0.0,
    magnetic_conductivity=0.0,
    specific_heat=730.0,
)
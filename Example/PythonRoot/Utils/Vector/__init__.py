# conceal the package available to use as a single module

from Utils.Vector.Vector import Vector
from Utils.Vector.Vector2D import Vector2D

__all__ = ["Vector", "Vector2D"]
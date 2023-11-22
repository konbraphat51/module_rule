# conceal the package available to use as a single module

from PythonRoot.Utils.Vector.Vector import Vector
from PythonRoot.Utils.Vector.Vector2D import Vector2D

__all__ = ["Vector", "Vector2D"]
# 5. If there are **sub-modules** of module A, **make a package** A and put them all in it. **And conceal the package able to used as a single module by `__init__.py`**

from A.AB.AB import ab

__all__ = ["ab"]
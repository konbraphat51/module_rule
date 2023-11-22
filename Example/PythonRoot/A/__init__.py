#5. **And conceal the package able to used as a single module by `__init__.py`**
from A.AA import aa
from A.AB import ab

__all__ = ["aa", "ab"]
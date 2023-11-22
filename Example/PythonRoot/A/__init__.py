#5. **And conceal the package able to used as a single module by `__init__.py`**
from PythonRoot.A.AA import aa
from PythonRoot.A.AB import ab

__all__ = ["aa", "ab"]
# 5. **And conceal the package able to used as a single module by `__init__.py`**
from PythonRoot.A.AB.ABA import aba

from PythonRoot.A.AB.AB_DataB import AB_DataB

def ab():
    aba()
    data = AB_DataB(None)
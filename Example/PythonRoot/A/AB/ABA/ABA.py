# 5. If there are **sub-modules** of module A, **make a package** A and put them all in it. **And conceal the package able to used as a single module by `__init__.py`**
# 6. If using the same level-1 directory module: import by **module** name
from A.AB.ABA.ABAA import abaa
from A.AB.ABA.ABAB import abab

def aba():
    abaa()
    abab()
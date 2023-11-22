# 3. **Only data-class direct-super-module** is **ALLOWED** to import; but any other else **direct-super-modules** are **NOT** allowed to import.
# 4. 4. If need to depend on another package, create/update the Modules Dependency UML of the **lowest-common** package.
from PythonRoot.A.AB.AB_DataA import AB_DataA

def abab():
    data = AB_DataA()
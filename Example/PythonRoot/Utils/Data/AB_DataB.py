#3. **Data-classes** must not depend on **logic-classes**, and should have each dependency UML for each level-1-directory.
from PythonRoot.A.AB.AB_DataA import AB_DataA

class AB_DataB():
    def __init__(self, data: AB_DataA):
        self.data = data
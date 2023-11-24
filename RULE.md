# Module Structure Rules

> [!WARNING]
> This `.md` is not edited yet.
>
> Edit all `EDIT` marked text and erace this note.

## Introduction

This is a rule for designing `Python` modules structure / adding `Python` modules to this project.

This is intended for avoiding

- inconsistent/messy `import`
- inconsistent/messy modules allocation
- circular `import`

## Rules

### Keys

1. [Basically depend on **sub-modules**. **Main module** should be the same name as the package(=directory) name, and the **sub-modules** in the **same directory**](#1-basically-depend-on-sub-modules-main-module-should-be-the-same-name-as-the-packagedirectory-name-and-the-sub-modules-in-the-same-directory)
2. [When depends on **co-level** (in the same directory) module, you **MUST** create/update the Dependency UML of that directory.](#2-when-depends-on-co-level-in-the-same-directory-module-you-must-createupdate-the-modules-dependency-uml-of-that-directory)
3. [**Only data-class** of super-modules is **ALLOWED** to import; but any other else **direct-super-modules** are **NOT** allowed to import.
   **Data-classes** must not depend on **logic-classes**, and should have each dependency UML for each level-1-directory.](#3-only-data-class-of-super-modules-is-allowed-to-import-but-any-other-else-direct-super-modules-are-not-allowed-to-import-data-classes-must-not-depend-on-logic-classes-and-should-have-each-dependency-uml-for-each-level-1-directory)
4. [If need to depend on another package, create/update the Modules Dependency UML of the **lowest-common** package.](#4-if-need-to-depend-on-another-package-createupdate-the-modules-dependency-uml-of-the-lowest-common-package)
5. [If there are **sub-modules** of module A, **make a package** A and put them all in it. **And conceal the package able to used as a single module by `__init__.py`**](#5-if-there-are-sub-modules-of-module-a-make-a-package-a-and-put-them-all-in-it-and-conceal-the-package-able-to-used-as-a-single-module-by-__init__py)
6. [If import the **co-directory module**: import by **module** name
   If import the **sub-directory**: import by **package** name (=sub-directory name)](#6-if-import-the-co-directory-module-import-by-module-name-if-import-the-sub-directory-import-by-package-name-sub-directory-name)
7. [If using another level-1 directory module: import by level-1 **package** name  
   If using the same level-1 directory module: import by **module** name](#7-if-using-another-level-1-directory-module-import-by-level-1-package-name-if-using-the-same-level-1-directory-module-import-by-module-name)

### Details

#### 1. Basically depend on **sub-modules**. **Main module** should be the same name as the package(=directory) name, and the **sub-modules** in the **same directory**

![image](https://github.com/konbraphat51/module_rule/assets/101827492/60e9ca70-6e8c-4e29-9c35-455a7dfcea85)

In this case,

- The **main module** of `ABA` package is **ABA.py**, and
- The **sub-modules** of `ABA.py` are **ABAA.py** and **ABAB.py**

`ABA.py` should import from `ABAA.py` or `ABAB.py` and **not from super-modules**.  
**Super-modules** of `ABA.py` are `AB.py` and `AA.py`

#### 2. When depends on **co-level** (in the same directory) module, you **MUST** create/update the Modules Dependency UML of that directory.

![image](https://github.com/konbraphat51/module_rule/assets/101827492/5c06ed97-eba3-41af-82cd-d350e5e221c2)

In here, `ABBA.py` and `ABBB.py` are **co-level** module.

In `ABBB.py`, there is:

```python
from PythonRoot.A.AB.ABB.ABBA import abba
```

This means `ABBB.py` is depending on `ABBA.py`

If there is other than sub -> main dependency within the package, [you have to draw a Dependency UML of the package](#drawing-dependency-uml).

In this case, the Dependency UML of `ABB` package will be:

![image](https://github.com/konbraphat51/module_rule/assets/101827492/43a23278-f0d9-4406-a4e0-85f5e09cd692)

#### 3. **Only data-class** of super-modules is **ALLOWED** to import; but any other else **direct-super-modules** are **NOT** allowed to import. **Data-classes** must not depend on **logic-classes**, and should have each dependency UML for each level-1-directory.

**Data-class** is a class to contain a data, not processing anything. Because this class will be an interface between modules, this is specially allowed to import from super-modules.

But **logid-class** (processing things) is not.

Denpendency UML of **All data class** should be drawn like this:  
![image](https://github.com/konbraphat51/module_rule/assets/101827492/efb16ffc-9bf8-4ede-80ab-854133cd3611)

#### 4. If need to depend on another package, create/update the Modules Dependency UML of the **lowest-common** package.

**lowest-common** means:  
 When `A->B` dependency, the lowest level directory of `A` and `B` exists.

When `A_A_A` depends on `A_B_B`, in the case below:  
![Image](https://user-images.githubusercontent.com/101827492/285468378-8136fd12-3065-419e-93cc-8a2729a641b8.png)  
the **lowest-common package** is `A_directory`

[Draw a dependency on the UML of **lowest-common package**](#drawing-dependency-uml)

#### 5. If there are **sub-modules** of module A, **make a package** A and put them all in it. **And conceal the package able to used as a single module by `__init__.py`**

If the package `A` is like this:  
![image](https://github.com/konbraphat51/module_rule/assets/101827492/136e7d9f-6b09-41f5-876b-d451dbaf3bee)

`AB` and `AC` are **sub-modules** of `AA`, so make a `AA` package like this:  
![image](https://github.com/konbraphat51/module_rule/assets/101827492/4421c74a-4ca2-4810-b1b6-fd1b8c5a4cdd)

And **conceal the structure of the sub-package**, and make it usable as a **module** by `__init__.py`

Write `AA\__init__.py` as:

```python
from A.AA.AA import aa
```

So, `A.py` can use it as

```python
from A.AA import aa
```

as if `AA` package were a module.

#### 6. If import the **co-directory module**: import by **module** name. If import the **sub-directory**: import by **package** name (=sub-directory name)

**module name** is refering the file path.  
**package name** is refering the directory path.

Example:
![image](https://github.com/konbraphat51/module_rule/assets/101827492/4421c74a-4ca2-4810-b1b6-fd1b8c5a4cdd)

```python
#module name
from A.AA.AA import aa

#package name
from A.AA import aa
```

Of course, to enable importing from **package** name, your wanted function/class should be in `__init__.py` of the package.

This rule is for avoiding circular reference.

#### 7. If using another level-1 directory module: import by level-1 **package** name. If using the same level-1 directory module: import by **module** name.

Among this example:  
![image](https://github.com/konbraphat51/module_rule/assets/101827492/ec92668f-ea44-404b-b32b-d28c91220f8e)

package `A` and `Utils` is **level-1-directory module**s.

If `ABAA.py` wants to import `Utils.Vector`(diffrent level-1-directory),

```python
#from package name
from PythonRoot.Utils import Vector
```

If `ABBA.py` wants to import `ABAA.py` (the same level-1-directory),

```python
#from module name
from PythonRoot.A.AB.ABA.ABAA import abaa
```

This rule is for avoiding circular reference.

[Don't forget to draw UML](#drawing-dependency-uml)

## Drawing Dependency UML

The main indent purpose of drawing Dependency UML is to **avoid circular dependency**.

If your UML has a cycle like this:  
![image](https://user-images.githubusercontent.com/101827492/285475790-9f48b8e2-6ea5-4f2d-9d0e-f54a92c832c6.png)

This means you have an circular dependency, which will typically make a system error.

Drive out every last of them.

[PlantUML](https://plantuml.com/en/) is recommended to use for drawing UML

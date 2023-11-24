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

1. Basically depend on **sub-modules**. **Main module** should be the same name as the package(=directory) name, and the **sub-modules** in the **same directory**
2. When depends on **co-level** (in the same directory) module, you **MUST** create/update the Modules Dependency UML of that directory.
3. **Only data-class direct-super-module** is **ALLOWED** to import; but any other else **direct-super-modules** are **NOT** allowed to import.  
   **Data-classes** must not depend on **logic-classes**, and should have each dependency UML for each level-1-directory.
4. If need to depend on another package, create/update the Modules Dependency UML of the **lowest-common** package.
5. If there are **sub-modules** of module A, **make a package** A and put them all in it. **And conceal the package able to used as a single module by `__init__.py`**
6. If import the **co-directory module**: import by **module** name  
   If import the **sub-directory**: import by **package** name (=sub-directory name)
7. If using another level-1 directory module: import by level-1 **package** name  
   If using the same level-1 directory module: import by **module** name

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

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

1. Basically depend on **sub-modules**
2. depends on **co-level** (in the same directory) module, you **MUST** create/update the Modules Dependency UML of that directory.
3. **Only data-class super-module** is **ALLOWED** to import; but any other else **super-modules** are **NOT** allowed to import.
4. If need to depend on another package (directory), create/update the Modules Dependency UML of the highest directory.
5. If there are **sub-modules** of module A, **make a package** A and put them all in it. **And make the package able to used as a single module by `__init__.py`**
6. If import the **co-level module**: import by **module** name  
   If import the **sub-module**: import by **package** name

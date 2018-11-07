# import-example
An example of how to build a conda reposity with a few nested files

Package structure:

```
ImportExample/
    README
    MANIFEST.in
    setup.py
    conda-recipe/
        bld.bat
        meta.yaml
    example_import
        __init__.py
        path1/
            __init__.py
            inner1.py
        path2/
            __init__.py
            inner2.py
        data/
            test.txt
```


Python files are included automatically.  
The MANIFEST.in file is used by setuptools to include additional files such as:
 - data/text.txt
 - this README

To build the conda tarball from `ImportExample/..` run:
```
conda-build ImportExample --output-folder %HOMEDRIVE%%HOMEPATH%\conda-bld
```

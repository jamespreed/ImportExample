from setuptools import setup, find_packages

setup(
    name='example_import',
    version='0.1.0',
    description='simple import test',
    packages=find_packages(),
    package_data={'example_import': ['data/*.txt']},
    python_requires=">=3.6",
    include_package_data=True
    )
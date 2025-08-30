from setuptools import setup, find_packages

with open("module_a/version.py") as f:
    exec(f.read())

setup(
    name="my-multi-module-project",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        # dependencies
    ],
)
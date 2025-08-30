from setuptools import setup
from pathlib import Path

version = Path(__file__).resolve().parent.parent / "Version"
version = version.read_text().strip()

setup(
    name="projectB",
    version=version,
    description="Project A managed by semantic-release",
     py_modules=["main"],
)
from setuptools import setup, find_packages

setup(
    name="versioning-package",          # نام بسته
    version="0.0.1",            # نسخه اولیه
    packages=find_packages(),   # شامل تمام پوشه‌های پایتون
    description="Test package for semantic-release",
)
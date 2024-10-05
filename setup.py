# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Read version from __init__.py
import re, ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('installment/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='installment',
    version=version,
    description='Help you sell in installment method',
    author='Ahmed Ragheb',
    author_email='kelshiekh@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
)
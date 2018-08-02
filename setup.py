#! /usr/bin/python
"""Setuptools-based setup script for datreant.data.

For a basic installation just type the command::

  python setup.py install

"""

from setuptools import setup, find_packages

print(find_packages())

setup(
    name="datreant_cli",
    version="0.7.0-dev",
    description="convenient CLI interface for Treant directories",
    author="Max Linke",
    author_email="max_linke@gmx.de",
    url="http://datreant.org/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    scripts=[],
    license="BSD",
    long_description=open("README.rst").read(),
    install_requires=["datreant", "six", "click"],
    entry_points={"console_scripts": ["dtr=datreant_cli.cli:cli"]},
)

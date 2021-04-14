#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="PCR_detective",
    version="0.0.1",
    author="",
    author_email="",
    license="GPLv3",
    description="",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["PCR_detective = src.__main__:main"]
    },
)

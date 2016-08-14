#!/usr/bin/python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages
import sys
import os
import os.path as path

setup(
    name = "dataUploader",
    version = "1.0.1",
    author = "Roman Dvorak",
    author_email = "roman-dvorak@email.cz",
    description = ("Software for backup data to space.astro.cz server"),
    license = "General Public License v3'",
    keywords = "ssh, backup, ",
    url = "http://wiki.bolidozor.cz",
    packages=[],
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: Czech',
        # 'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
#!/usr/bin/python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages
import sys
import os
import os.path as path


os.chdir(path.realpath(path.dirname(__file__)))
sys.path.insert(1, 'src')
import rmds_data_uploader


setup(
    name             = 'rmds_data_uploader',
    version          = rmds_data_uploader.__version__,
    author           = 'Jan Milík',
    author_email     = 'milikjan@fit.cvut.cz',
    description      = 'Common tools and functions for MLAB python modules.',
    long_description = rmds_data_uploader.__doc__,
    url              = 'https://github.com/bolidozor/RMDS-data-uploader',
    
    #packages    = ['pymlab', 'pymlab.sensors', 'pymlab.tests', ],
    packages    = find_packages("src"),
    package_dir = {'': 'src'},
    provides    = ['rmds_data_uploader'],
    install_requires = [ 'mlabutils', 'python-daemon', 'lockfile', ],
    keywords = ['MLAB', 'bolidozor', ],
    license     = 'Lesser General Public License v3',
    #download_url = 'https://github.com/bolidozor/RMDS-data-uploader',
    
    test_suite = 'tests',
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: Czech',
        # 'Operating System :: OS Independent',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)


#!/usr/bin/env python

from setuptools import setup

import baas32


setup(
    name='baas32',
    version='0.3.1',
    description=("An alternative Python implementation of Douglas Crockford's "
                 "base32 encoding scheme"),
    long_description=baas32.__doc__,
    license='BSD',
    author='Bas van den Heuvel',
    author_email='vdheuvel.bas@gmail.com',
    url='https://github.com/klaplong/baas32.git',
    download_url='https://pypi.python.org/pypi/baas32/',
    py_modules=['baas32'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)

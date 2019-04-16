#!/usr/bin/env python3

"""Test, build, or install the Shadowbot package.

Run tests:
  python setup.py test

Build and install:
  python setup.py build && python setup.py install
"""

from distutils.util import convert_path
from setuptools import setup, find_packages

VER_FILEPATH = convert_path('shadowbot/version.txt')
with open(VER_FILEPATH) as file:
    __version__ = file.read()

print(__version__)

setup(
    name='Shadowbot',
    description='A "shadowplay for voice" Discord bot',
    url='https://shadowbot.io',
    author='Steven Burnett',
    author_email='steven@shadowbot.io',
    license='GPLv3',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=[
        'coverage',
        'pytest',
        'pytest-cov',
        'pytest-pylint'
    ],
    version=__version__,
)

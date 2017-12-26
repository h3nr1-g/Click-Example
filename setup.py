import os
from setuptools import setup
import sys

if sys.version_info < (3, 4):
    print('clickdemo requires Python 3.4 or higher')
    exit(-1)

with open('requirements.txt') as fh:
    required = fh.read().splitlines()

setup(
    name='greeter',
    version='1.0.0',
    packages=['greeter', 'greeter.commands'],
    include_package_data=True,
    install_requires=required,
    entry_points='''
        [console_scripts]
        greeter=greeter.greeter:cli
    ''',
)

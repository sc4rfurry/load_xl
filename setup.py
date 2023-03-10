#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


setup(
    name='load_xl',
    version='0.2.0',
    description='A library for parsing .envi files and configuration files. Also includes functions for parsing .ini, .yaml, and .json files.',
    long_description=open('README.md').read() + '\n\n',
    long_description_content_type="text/markdown",
    author='sc4rfurry',
    author_email='akalucifr@protonmail.ch',
    url='https://github.com/sc4rfurry',
    packages=find_packages(),
    classifiers=classifiers,
    keywords=['env', 'env_loader', 'config', 'config_parser', 'parser'],
    install_requires=['pyyaml', 'wheel'],
)
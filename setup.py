#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="load_xl",
    version="1.0.1",
    description="A library for parsing configuration files, including .env, .ini, .yaml, .json, .toml, and .xml formats.",
    long_description=open("README.md").read() + "\n\n",
    long_description_content_type="text/markdown",
    author="sc4rfurry",
    author_email="akalucifr@protonmail.ch",
    url="https://github.com/sc4rfurry/load_xl",
    packages=find_packages(),
    classifiers=classifiers,
    keywords=[
        "config",
        "configuration",
        "parser",
        "env",
        "ini",
        "yaml",
        "json",
        "toml",
        "xml",
    ],
    install_requires=["pyyaml", "jsonschema", "watchdog", "toml"],
    entry_points={
        "console_scripts": [
            "load_xl=load_xl:cli",
        ],
    },
    python_requires=">=3.6",
)

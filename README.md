# **load_xl** - A Python Configuration Parser Library

`load_xl` is a simple and easy to use library for parsing environment variable and configuration files in `Python`. It provides a convenient way to load environment variables from .envi files and parse unique syntax configuration files.
> **Note:** This library is still in development and is not yet ready for production use. Go to [pypi](https://pypi.org/project/load-xl/) to install the latest version and visit [load_xl](https://sc4rfurry.github.io/get_load_xl/) webite.

#
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example Code](#example-code)
- [Supported File Types](#supported-file-types)
- [Pypi Package](#pypi-package)
- [Error and Exception handling](#error-and-exception-handling)
- [Change Log](#change-log)
#
## Installation

The package can be installed using pip.
```bash
pip3 install load-xl
OR
python3 -m pip install load-xl
```

## Usage

Here's how to use load_xl in your Python code:

```python

import load_xl
# Load environment variables from .envi file
load_xl.load_envi_file('.envi')

# Read configuration file
config = load_xl.read_config_file('.configx')
```

+ The `load_envi_file` function takes a file path to a .envi file and loads the defined environment variables to the environment.

+ The `read_config_file` function takes a file path to a unique syntax configuration file and returns a dictionary of all the keys and values defined in the file.
.envi file format

The .envi file should contain one environment variable per line in the following format:

```bash
# Key and Value
KEY=VALUE
```

Lines starting with a # symbol will be ignored as comments.
Unique syntax configuration file format

The unique syntax configuration file should follow the following rules:

+ Lines starting with a - symbol are treated as environment variables and split on the : sign.
+ Lines starting with & or % are ignored as comments.
+ Only values that start with $ are taken into consideration.

### Example (`.configx` file format)
```bash
# This is a comment line, ignored by the parser
& This is a comment line &, ignored by the parser
% This is a comment line %, ignored by the parser


# Keys and Values
$ key1: value1 # Returns value1
$ key2: value2
- key3: value3 # Sets environment variable key3 to value3
```
#

## Supported File Types
- .envi
- .configx
- .ini
- .yaml
- .json
#

## Example Code:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import load_xl
import os



# Test envi file parsing and loading into os.environ
try:
    print("\n[+] Loading envi file...")
    load_xl.load_envi_file('.envi')
    print(os.environ['TEST'])
    print(os.environ['TEST_ENV'])
except load_xl.EnviFileParsingError as e:
    print("Error in parsing envi file: {e}")


# Test config file parsing and loading into os.environ
try:
    print("\n[+] Loading config file...")
    print(load_xl.read_config_file('.configx'))
    print(os.environ['CONFIG_ENV'])
except load_xl.ConfigFileParsingError as e:
    print('Error in parsing config file: {e}')


# Test ini file parsing and returning as dict
try:
    print("\n[+] Loading ini file...")
    ini_file = load_xl.load_ini_file('.ini')
    print(ini_file)
except load_xl.IniFileParsingError as e:
    print('Error in parsing ini file: {e}')


# Test yaml file parsing and returning as dict
try:
    print("\n[+] Loading yaml file...")
    yaml_file = load_xl.load_yaml_file('.yaml')
    print(yaml_file)
except load_xl.YamlFileParsingError as e:
    print('Error in parsing yaml file: {e}')


# Test json file parsing and returning as dict
try:
    print("\n[+] Loading json file...")
    json_data = load_xl.load_json_file('.json')
    print(json_data)
except load_xl.JsonFileParsingError as e:
    print('Error in parsing json file: {e}')
```
#
## Pypi Package
- You can install this as a python3 library at [pypi](https://pypi.org/project/load-xl/) 

[![PyPI version](https://badge.fury.io/py/load-xl.svg)](https://badge.fury.io/py/load-xl)

#
## Error and Exception handling

The library provides a comprehensive error and exception handling mechanism to ensure the stability and reliability of your code.


# Change Log
==============

0.1.0 (06/02/2023)
-------------------
- initial release

0.1.1 (06/02/2023)
-------------------
- Fixed README.md

0.2.0 (07/02/2023)
-------------------
- Fixed Some Bugs
- Now you can load any `.ini`, `.yaml` and `.json` file directely
- Check `tests` folder for example usage

## Contributing

If you want to contribute to load_xl, please reach out to the maintainers. We welcome contributions, bug reports, and feedback.

## License
load_xl is released under the MIT License.
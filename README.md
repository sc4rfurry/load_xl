# `load_xl` - A Python Configuration Parser Library

load_xl is a simple and easy to use library for parsing environment variable and configuration files in `Python`. It provides a convenient way to load environment variables from .envi files and parse unique syntax configuration files.
Installation

The package can be installed using pip.
```bash
pip install load-xl
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

### Example
```bash
# This is a comment line, ignored by the parser
& This is a comment line &, ignored by the parser
% This is a comment line %, ignored by the parser


# Keys and Values
$ key1: value1 # This line follows the correct syntax for key-value pair
$ key2: value2
- key3: value3 # This line follows the correct syntax for environment variable
```

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
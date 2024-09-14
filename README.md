```
 _                    _          _
| |    ___   __ _  __| |   __  _| |
| |   / _ \ / _` |/ _` |   \ \/ / |
| |__| (_) | (_| | (_| |    >  <| |
|_____\___/ \__,_|\__,_|   /_/\_\_|

   Configuration Parser Extraordinaire
```

# load_xl

[![PyPI version](https://badge.fury.io/py/load-xl.svg)](https://badge.fury.io/py/load-xl)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/load-xl.svg)](https://pypi.org/project/load-xl/)

`load_xl` is a versatile Python library for parsing various configuration file formats, including `.env`, `.ini`, `.yaml`, `.json`, `.toml`, and `.xml`. It provides a unified interface for loading and validating configuration data, making it easy to work with different file formats in your projects.

## ✨ Features

```
┌─────────────────────────────────────────────┐
│ ⚙️  Multiple configuration file formats      │
│ 🔄 Automatic environment variable substition │
│ 🛡️  JSON Schema validation                   │
│ 🔍 File watching for auto config reloading   │
│ 🖥️  Command-line interface (CLI)             │
│ 🐍 Compatible with Python 3.6+               │
└─────────────────────────────────────────────┘
```

## 🚀 Installation

Install `load_xl` using pip:

```bash
pip install load-xl
```

## 💻 Usage

### As a Library

```python
from load_xl import load_config

# Load a configuration file
config = load_config('path/to/your/config.yaml')

# Load with schema validation
schema = {...}  # Your JSON schema
config = load_config('path/to/your/config.json', schema=schema)

# Access configuration data
print(config['some_key'])
```

### Command-line Interface

```bash
load_xl path/to/your/config.yaml --output
load_xl path/to/your/config.json --validate --schema path/to/schema.json
```

## 📁 Supported File Formats

```
┌─────┬───────────────────────────────┐
│.env │ Environment variables         │
│.ini │ INI configuration files       │
│.yaml│ YAML configuration files      │
│.json│ JSON configuration files      │
│.toml│ TOML configuration files      │
│.xml │ XML configuration files       │
└─────┴───────────────────────────────┘
```

## 🔬 Testing

The `load_xl` library includes a comprehensive test suite. You can find the test script in the `test` directory. Here's a snippet of the `test.py` file:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from load_xl import load_config, FileParsingError

# Test .env file parsing and loading
try:
    print("\n[+] Loading .env file...")
    env_config = load_config(".env")
    print(env_config.get("TEST"))
    print(env_config.get("TEST_ENV"))
except FileParsingError as e:
    print(f"Error in parsing .env file: {e}")

# ... (tests for other file formats)

# Test .xml file parsing and returning as dict
try:
    print("\n[+] Loading .xml file...")
    xml_config = load_config("test.xml")
    print(xml_config)
except FileParsingError as e:
    print(f"Error in parsing .xml file: {e}")
```

To run the tests, navigate to the `test` directory and execute:

```bash
python test.py
```

## 🔧 Advanced Features

### Environment Variable Substitution

`load_xl` automatically replaces `${VAR}` patterns in your configuration files with the corresponding environment variable values.

### File Watching

```python
from load_xl import ConfigFileWatcher, YamlFileParser

watcher = ConfigFileWatcher('config.yaml', YamlFileParser)
watcher.start()

# Your application logic here

watcher.stop()
```
##

> **Note:** There are example schema files provided in **schemas** folder.
##


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **sc4rfurry** - [GitHub](https://github.com/sc4rfurry)

## 🙏 Acknowledgments

- Thanks to all contributors and users of `load_xl`
- Inspired by the need for a unified configuration parsing solution
- This project was developed with some assistance from **ChatGPT 4.0** , showcasing the potential of AI-assisted coding and for my peronal experience too

---

For more information and updates, please visit the [GitHub repository](https://github.com/sc4rfurry/load_xl).

```
 ______________________________
< Thank you for using load_xl! >
 ------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

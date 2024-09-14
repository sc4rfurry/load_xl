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


# Test .ini file parsing and returning as dict
try:
    print("\n[+] Loading .ini file...")
    ini_config = load_config("test.ini")
    print(ini_config)
except FileParsingError as e:
    print(f"Error in parsing .ini file: {e}")

# Test .yaml file parsing and returning as dict
try:
    print("\n[+] Loading .yaml file...")
    yaml_config = load_config("test.yaml")
    print(yaml_config)
except FileParsingError as e:
    print(f"Error in parsing .yaml file: {e}")

# Test .json file parsing and returning as dict
try:
    print("\n[+] Loading .json file...")
    json_config = load_config("test.json")
    print(json_config)
except FileParsingError as e:
    print(f"Error in parsing .json file: {e}")

# Test .toml file parsing and returning as dict
try:
    print("\n[+] Loading .toml file...")
    toml_config = load_config("test.toml")
    print(toml_config)
except FileParsingError as e:
    print(f"Error in parsing .toml file: {e}")

# Test .xml file parsing and returning as dict
try:
    print("\n[+] Loading .xml file...")
    xml_config = load_config("test.xml")
    print(xml_config)
except FileParsingError as e:
    print(f"Error in parsing .xml file: {e}")

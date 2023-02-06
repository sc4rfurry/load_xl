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
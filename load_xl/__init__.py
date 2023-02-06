#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import yaml
import json


__version__ = '0.1.1'
__all__ = ['load_envi_file', 'read_config_file','load_ini_file', 'load_yaml_file', 'load_json_file', 'EnviFileParsingError', 'ConfigFileParsingError', 'IniFileParsingError', 'YamlFileParsingError', 'JsonFileParsingError']



class EnviFileParsingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message
    def __unicode__(self):
        return self.message
    def __bytes__(self):
        return self.message.encode('utf-8')
    def __format__(self, format_spec):
        return self.message.format(format_spec)



class ConfigFileParsingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message
    def __unicode__(self):
        return self.message
    def __bytes__(self):
        return self.message.encode('utf-8')
    def __format__(self, format_spec):
        return self.message.format(format_spec)
    
class IniFileParsingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message
    def __unicode__(self):
        return self.message
    def __bytes__(self):
        return self.message.encode('utf-8')
    def __format__(self, format_spec):
        return self.message.format(format_spec)

class YamlFileParsingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message
    def __unicode__(self):
        return self.message
    def __bytes__(self):
        return self.message.encode('utf-8')
    def __format__(self, format_spec):
        return self.message.format(format_spec)
    

class JsonFileParsingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message
    def __unicode__(self):
        return self.message
    def __bytes__(self):
        return self.message.encode('utf-8')
    def __format__(self, format_spec):
        return self.message.format(format_spec)




class IniFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def parse(self):
        try:
            with open(self.file_path, 'r') as file:
                current_section = ''
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if line.startswith('['):
                        current_section = line[1:-1].strip()
                        self.config[current_section] = {}
                    else:
                        key, value = line.split('=', 1)
                        self.config[current_section][key.strip()] = value.strip()
        except Exception as e:
            raise Exception(f"Error in parsing .ini file: {e}")

    def load(self):
        try:
            self.parse()
        except Exception as e:
            raise Exception(f"Error in loading .ini file: {e}")

    def get_config(self):
        try:
            self.load()
            return self.config
        except Exception as e:
            raise Exception(f"Error in returning config in JSON format: {e}")
    



class YamlFileParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        try:
            with open(self.file_path, 'r') as file:
                self.config = yaml.safe_load(file)
        except Exception as e:
            raise Exception(f"Error in parsing .yaml file: {e}")

    def load(self):
        try:
            self.parse()
        except Exception as e:
            raise Exception(f"Error in parsing .yaml file: {e}")

    def get_config(self):
        try:
            self.load()
            return self.config
        except Exception as e:
            raise Exception(f"Error in returning config in JSON format: {e}")
        



class JsonFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def parse(self):
        try:
            with open(self.file_path, 'r') as file:
                self.config = json.load(file)
        except Exception as e:
            raise Exception(f"Error in parsing .json file: {e}")

    def load(self):
        try:
            self.parse()
        except Exception as e:
            raise Exception(f"Error in loading .json file: {e}")
    
    def get_config(self):
        try:
            self.load()
            return self.config
        except Exception as e:
            raise Exception(f"Error in returning config in JSON format: {e}")
    



class EnviFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def parse(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    key, value = line.split('=', 1)
                    self.config[key.strip()] = value.strip()
        except Exception as e:
            raise EnviFileParsingError(f"Error in parsing envi file: {e}")

    def load(self):
        try:
            self.parse()
            for key, value in self.config.items():
                os.environ[key] = value
        except EnviFileParsingError as e:
            print(e)
    
    def get_config(self):
        try:
            self.load()
            return self.config
        except EnviFileParsingError as e:
            raise Exception(f"Error in returning config in JSON format: {e}")




class ConfigFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}


    def load(self):
        try:
            self.parse()
        except ConfigFileParsingError as e:
            print(e)


    def parse(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('&') or line.startswith('%'):
                        continue
                    if line.startswith('$'):
                        key, value = line[1:].split(':', 1)
                        self.config[key.strip()] = value.strip()
                    elif line.startswith('-'):
                        key, value = line[1:].split(':', 1)
                        os.environ[key.strip()] = value.strip()
        except Exception as e:
            raise ConfigFileParsingError(f"Error in parsing config file: {e}")

    def get_config(self):
        try:
            self.load()
            return self.config
        except Exception as e:
            raise Exception(f"Error in returning config file: {e}")




def load_envi_file(file_path):
    envi_file_parser = EnviFileParser(file_path)
    envi_file_parser.get_config()

def read_config_file(file_path):
    config_file_parser = ConfigFileParser(file_path)
    return config_file_parser.get_config()

def load_yaml_file(file_path):
    yaml_file_parser = YamlFileParser(file_path)
    return yaml_file_parser.get_config()

def load_json_file(file_path):
    json_file_parser = JsonFileParser(file_path)
    return json_file_parser.get_config()

def load_ini_file(file_path):
    ini_file_parser = IniFileParser(file_path)
    return ini_file_parser.get_config()
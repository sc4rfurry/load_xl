#!/usr/bin/env python3
import os


__all__ = ['load_envi_file', 'read_config_file']



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
            print(f"Error in parsing file: {e}")

    def load(self):
        self.parse()
        for key, value in self.config.items():
            os.environ[key] = value

class ConfigFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}


    def read(self):
        self.parse()
        return self.config


    def parse(self):
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


def load_envi_file(file_path):
    envi_file_parser = EnviFileParser(file_path)
    envi_file_parser.load()

def read_config_file(file_path):
    config_file_parser = ConfigFileParser(file_path)
    return config_file_parser.read()

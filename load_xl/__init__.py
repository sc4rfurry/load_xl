#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
import json
import toml
import xml.etree.ElementTree as ET
import logging
import re
from jsonschema import validate, ValidationError
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# Set up secure logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)

__version__ = "1.0.1"


# --- Exception Classes ---
class FileParsingError(Exception):
    """Base class for file parsing errors."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class UnsupportedFileTypeError(FileParsingError):
    pass


class SchemaValidationError(FileParsingError):
    pass


# --- Mixin for Environment Variable Substitution ---
class EnvSubstitutionMixin:
    ENV_PATTERN = re.compile(r"\$\{(\w+)\}")

    def substitute_env_vars(self, config):
        """Recursively replace ${VAR} with environment variables in config dictionary."""

        def _substitute(value):
            if isinstance(value, str):
                match = self.ENV_PATTERN.match(value)
                if match:
                    env_var = os.getenv(match.group(1), value)
                    if not env_var:
                        raise FileParsingError(
                            f"Environment variable {match.group(1)} not found."
                        )
                    return env_var
            return value

        def _replace_in_dict(d):
            for k, v in d.items():
                if isinstance(v, dict):
                    d[k] = _replace_in_dict(v)
                elif isinstance(v, list):
                    d[k] = [_substitute(i) for i in v]
                else:
                    d[k] = _substitute(v)
            return d

        return _replace_in_dict(config)


# --- Config File Parsers ---
class IniFileParser(EnvSubstitutionMixin):
    def __init__(self, file_path):
        self.file_path = Path(file_path)  
        self.config = {}

    def parse(self):
        """Parse INI file and populate self.config."""
        try:
            with self.file_path.open(
                "r"
            ) as file:
                current_section = ""
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if line.startswith("["):
                        current_section = line[1:-1].strip()
                        self.config[current_section] = {}
                    else:
                        if "=" not in line:
                            raise FileParsingError(
                                f"Malformed line in INI file: {line}"
                            )
                        key, value = line.split("=", 1)
                        self.config[current_section][key.strip()] = value.strip()
        except FileNotFoundError:
            raise FileParsingError(f"INI file not found: {self.file_path}")
        except PermissionError:
            raise FileParsingError(f"Permission denied: {self.file_path}")
        except Exception as e:
            raise FileParsingError(f"Error parsing INI file: {str(e)}")

    def load(self):
        self.parse()

    def get_config(self):
        self.load()
        return self.substitute_env_vars(self.config)


class YamlFileParser(EnvSubstitutionMixin):
    def __init__(self, file_path, schema=None):
        self.file_path = Path(file_path)  
        self.schema = schema
        self.config = {}

    def parse(self):
        """Parse YAML file and populate self.config."""
        try:
            with self.file_path.open("r") as file:
                self.config = yaml.safe_load(file)
                if self.schema:
                    self.validate_schema()
        except FileNotFoundError:
            raise FileParsingError(f"YAML file not found: {self.file_path}")
        except PermissionError:
            raise FileParsingError(f"Permission denied: {self.file_path}")
        except yaml.YAMLError as e:
            raise FileParsingError(f"YAML parsing error: {str(e)}")
        except Exception as e:
            raise FileParsingError(f"Error parsing YAML file: {str(e)}")

    def validate_schema(self):
        """Validate the parsed config against a JSON schema."""
        try:
            validate(instance=self.config, schema=self.schema)
        except ValidationError as e:
            raise SchemaValidationError(f"Schema validation error: {e.message}")

    def load(self):
        self.parse()

    def get_config(self):
        self.load()
        return self.substitute_env_vars(self.config)


class JsonFileParser(EnvSubstitutionMixin):
    def __init__(self, file_path, schema=None):
        self.file_path = Path(file_path)  
        self.schema = schema
        self.config = {}

    def parse(self):
        """Parse JSON file and populate self.config."""
        try:
            with self.file_path.open("r") as file:
                self.config = json.load(file)
                if self.schema:
                    self.validate_schema()
        except FileNotFoundError:
            raise FileParsingError(f"JSON file not found: {self.file_path}")
        except PermissionError:
            raise FileParsingError(f"Permission denied: {self.file_path}")
        except json.JSONDecodeError as e:
            raise FileParsingError(f"JSON parsing error: {str(e)}")
        except Exception as e:
            raise FileParsingError(f"Error parsing JSON file: {str(e)}")

    def validate_schema(self):
        """Validate the parsed config against a JSON schema."""
        try:
            validate(instance=self.config, schema=self.schema)
        except ValidationError as e:
            raise SchemaValidationError(f"Schema validation error: {e.message}")

    def load(self):
        self.parse()

    def get_config(self):
        self.load()
        return self.substitute_env_vars(self.config)


class TomlFileParser(EnvSubstitutionMixin):
    def __init__(self, file_path):
        self.file_path = Path(file_path)  
        self.config = {}

    def parse(self):
        """Parse TOML file and populate self.config."""
        try:
            with self.file_path.open("r") as file:
                self.config = toml.load(file)
        except FileNotFoundError:
            raise FileParsingError(f"TOML file not found: {self.file_path}")
        except PermissionError:
            raise FileParsingError(f"Permission denied: {self.file_path}")
        except toml.TomlDecodeError as e:
            raise FileParsingError(f"TOML parsing error: {str(e)}")
        except Exception as e:
            raise FileParsingError(f"Error parsing TOML file: {str(e)}")

    def load(self):
        self.parse()

    def get_config(self):
        self.load()
        return self.substitute_env_vars(self.config)


class XmlFileParser(EnvSubstitutionMixin):
    def __init__(self, file_path):
        self.file_path = Path(file_path)  
        self.config = {}

    def parse(self):
        """Parse XML file and populate self.config."""
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            self.config = self._xml_to_dict(root)
        except FileNotFoundError:
            raise FileParsingError(f"XML file not found: {self.file_path}")
        except PermissionError:
            raise FileParsingError(f"Permission denied: {self.file_path}")
        except ET.ParseError as e:
            raise FileParsingError(f"XML parsing error: {str(e)}")
        except Exception as e:
            raise FileParsingError(f"Error parsing XML file: {str(e)}")

    def _xml_to_dict(self, root):
        """Helper function to convert XML tree to dictionary."""
        return {child.tag: child.text for child in root}

    def load(self):
        self.parse()

    def get_config(self):
        self.load()
        return self.substitute_env_vars(self.config)


class EnviFileParser(EnvSubstitutionMixin):
    def __init__(self, file_path):
        self.file_path = Path(file_path)  
        self.config = {}

    def parse(self):
        """Parse .env file and populate self.config."""
        try:
            with self.file_path.open("r") as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" not in line:
                        raise FileParsingError(f"Malformed line in .env file: {line}")
                    key, value = line.split("=", 1)
                    self.config[key.strip()] = value.strip()
        except FileNotFoundError:
            raise FileParsingError(f".env file not found: {self.file_path}")
        except PermissionError:
            raise FileParsingError(f"Permission denied: {self.file_path}")
        except Exception as e:
            raise FileParsingError(f"Error parsing .env file: {str(e)}")

    def load(self):
        self.parse()

    def get_config(self):
        self.load()
        return self.substitute_env_vars(self.config)


# --- Unified Config Loader ---
def load_config(file_path, schema=None):
    """Load config from a file based on its extension."""
    file_path = Path(file_path)  # Ensure cross-platform path handling
    filename = file_path.name
    if filename == ".env":
        return EnviFileParser(file_path).get_config()
    else:
        extension = file_path.suffix.lower()  # Get file extension
    try:
        if extension == ".json":
            return JsonFileParser(file_path, schema=schema).get_config()
        elif extension == ".ini":
            return IniFileParser(file_path).get_config()
        elif extension in [".yaml", ".yml"]:
            return YamlFileParser(file_path, schema=schema).get_config()
        elif extension == ".toml":
            return TomlFileParser(file_path).get_config()
        elif extension == ".xml":
            return XmlFileParser(file_path).get_config()
        else:
            raise UnsupportedFileTypeError(f"Unsupported file type: {extension}")
    except FileParsingError as e:
        logging.error(e)
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise


# --- File Watcher for Automatic Reload ---
class ConfigFileWatcher(FileSystemEventHandler):
    def __init__(self, file_path, parser_class, schema=None):
        self.file_path = Path(file_path)  
        self.parser = parser_class(self.file_path, schema=schema)
        self.config = self.parser.get_config()
        self.observer = Observer()

    def on_modified(self, event):
        if Path(event.src_path) == self.file_path:
            logging.info(f"{self.file_path} has been modified, reloading...")
            self.config = self.parser.get_config()

    def start(self):
        self.observer.schedule(self, path=str(self.file_path.parent), recursive=False)
        self.observer.start()

    def stop(self):
        self.observer.stop()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import logging
from load_xl import load_config, FileParsingError

def cli():
    parser = argparse.ArgumentParser(description="Configuration File Parser CLI")
    parser.add_argument("file", help="Path to the configuration file")
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate configuration file with schema",
    )
    parser.add_argument("--schema", help="Path to the schema file for validation")
    parser.add_argument(
        "--output", action="store_true", help="Print parsed configuration"
    )

    args = parser.parse_args()

    try:
        schema = None
        if args.schema:
            with open(args.schema, "r") as schema_file:
                schema = json.load(schema_file)

        config = load_config(args.file, schema=schema)

        if args.validate:
            print("Configuration is valid.")

        if args.output:
            print(config)

    except FileParsingError as e:
        logging.error(f"Error parsing file: {str(e)}")
        print(f"Error: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    cli()

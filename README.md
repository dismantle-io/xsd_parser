# XSD to JSON Parser

This utility allows you to convert XML Schema Definition (XSD) files to JSON format. It uses the `lxml` library for parsing XSD and the built-in `json` module for writing the output.

## Installation

1. Clone this repository:

2. Navigate to the project directory:

3. Install the required libraries:
   ```pip install lxml```

## Usage

1. Run the script:
   ```python xsd_parser.py```
2. Enter the path to the XSD file when prompted. The script will produce a JSON file with the same name as the input file, but with a `.json` extension.

## Notes

This parser is basic and might not cover all XSD structures or semantics. It's recommended to enhance it based on specific needs or to handle more intricate XSD structures.

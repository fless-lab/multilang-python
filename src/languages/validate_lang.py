import json
import jsonschema
import os
import sys
from multilang_python.core.utils import read_file

def validate_language_file(lang_file):
    """Validate a language JSON file against schema and template."""
    # Load schema
    schema_file = os.path.join(os.path.dirname(__file__), 'schema.json')
    schema = read_file(schema_file, as_json=True)

    # Load template
    template_file = os.path.join(os.path.dirname(__file__), 'template.json')
    template = read_file(template_file, as_json=True)

    # Load language file
    try:
        lang_data = read_file(lang_file, as_json=True)
    except json.JSONDecodeError:
        print(f"Error: {lang_file} is not a valid JSON file.")
        sys.exit(1)

    # Validate against schema
    try:
        jsonschema.validate(instance=lang_data, schema=schema)
    except jsonschema.ValidationError as e:
        print(f"Error: {lang_file} is invalid: {e.message}")
        sys.exit(1)

    # Validate mappings against template
    for category in ['keywords', 'builtins']:
        template_values = template.get(category, [])
        for native, python in lang_data.get(category, {}).items():
            if python not in template_values:
                print(f"Error: {lang_file} contains invalid {category} mapping: '{native}' -> '{python}'")
                sys.exit(1)

    print(f"Language file {lang_file} is valid.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_lang.py <language_file>")
        sys.exit(1)
    validate_language_file(sys.argv[1])
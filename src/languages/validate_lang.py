import json
import sys
import os
from multilang_python.core.validator import LanguageValidator
from multilang_python.core.errors import ValidationError

def validate_language_file(file_path):
    """Validate a language JSON file."""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        lang_data = json.load(f)

    validator = LanguageValidator()
    try:
        validator.validate(lang_data)
        print(f"Language file {file_path} is valid.")
    except ValidationError as e:
        print(f"Validation error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_lang.py <language_file>")
        sys.exit(1)
    validate_language_file(sys.argv[1])
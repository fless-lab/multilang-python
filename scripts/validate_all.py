#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate all language files in the languages directory.
"""

import json
import os
import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def validate_language_file(lang_file, template, schema):
    """Validate a single language file."""
    errors = []
    warnings = []

    try:
        with open(lang_file, 'r', encoding='utf-8') as f:
            lang_data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"], []
    except Exception as e:
        return [f"Error reading file: {e}"], []

    # Check required sections
    required_sections = schema.get('required', [])
    for section in required_sections:
        if section not in lang_data:
            errors.append(f"Missing required section: {section}")
        elif not isinstance(lang_data[section], dict):
            errors.append(f"Section '{section}' must be a dictionary")
        elif not lang_data[section]:
            warnings.append(f"Section '{section}' is empty")

    # Validate mappings against template
    for category in ['keywords', 'builtins']:
        if category not in lang_data:
            continue

        template_items = template.get(category, [])

        # Check for missing translations
        for python_keyword in template_items:
            if python_keyword not in lang_data[category]:
                warnings.append(f"Missing {category} translation: {python_keyword}")

        # Check for invalid mappings
        for native_word, python_word in lang_data[category].items():
            if python_word not in template_items:
                errors.append(f"Invalid {category} mapping: '{native_word}' -> '{python_word}' (not in template)")

            # Check that native word is a valid Python identifier
            if not (native_word.isidentifier() or native_word in ['True', 'False', 'None']):
                errors.append(f"Invalid identifier in {category}: '{native_word}'")

    # Check for duplicate translations
    for category in ['keywords', 'builtins']:
        if category not in lang_data:
            continue

        translations = list(lang_data[category].values())
        duplicates = [t for t in set(translations) if translations.count(t) > 1]

        if duplicates:
            for dup in duplicates:
                python_words = [k for k, v in lang_data[category].items() if v == dup]
                warnings.append(f"Duplicate translation in {category}: '{dup}' used for {python_words}")

    return errors, warnings

def main():
    """Main entry point."""
    print("=" * 70)
    print("  multilang-python: Language File Validation")
    print("=" * 70)

    # Load template and schema
    lang_dir = os.path.join(os.path.dirname(__file__), '..', 'src', 'languages')
    template_file = os.path.join(lang_dir, 'template.json')
    schema_file = os.path.join(lang_dir, 'schema.json')

    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template = json.load(f)
    except Exception as e:
        print(f"[ERROR] Error loading template: {e}")
        sys.exit(1)

    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = json.load(f)
    except Exception as e:
        print(f"[ERROR] Error loading schema: {e}")
        sys.exit(1)

    # Find all language files
    lang_files = list(Path(lang_dir).glob('*.json'))
    lang_files = [f for f in lang_files if f.name not in ['template.json', 'schema.json']]

    if not lang_files:
        print("\n[WARNING] No language files found.")
        sys.exit(0)

    print(f"\n[INFO] Found {len(lang_files)} language file(s) to validate\n")

    # Validate each file
    total_errors = 0
    total_warnings = 0
    results = []

    for lang_file in sorted(lang_files):
        lang_code = lang_file.stem
        print(f"Validating {lang_code}.json...", end=' ')

        errors, warnings = validate_language_file(lang_file, template, schema)

        total_errors += len(errors)
        total_warnings += len(warnings)

        if errors:
            print("[FAILED]")
            results.append((lang_code, errors, warnings))
        elif warnings:
            print("[WARNING]")
            results.append((lang_code, errors, warnings))
        else:
            print("[PASSED]")

    # Print detailed results
    if results:
        print("\n" + "=" * 70)
        print("DETAILED RESULTS")
        print("=" * 70)

        for lang_code, errors, warnings in results:
            print(f"\nFile: {lang_code}.json:")

            if errors:
                print("  Errors:")
                for error in errors:
                    print(f"    - {error}")

            if warnings:
                print("  Warnings:")
                for warning in warnings:
                    print(f"    - {warning}")

    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files validated: {len(lang_files)}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")

    if total_errors > 0:
        print("\n[FAILED] Validation failed with errors.")
        sys.exit(1)
    elif total_warnings > 0:
        print("\n[WARNING] Validation passed with warnings.")
        sys.exit(0)
    else:
        print("\n[SUCCESS] All validations passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()

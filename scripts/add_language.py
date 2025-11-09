#!/usr/bin/env python3
"""
Interactive tool to add a new language to multilang-python.
"""

import json
import os
import sys

def load_template():
    """Load the template with all required keywords and builtins."""
    template_path = os.path.join(
        os.path.dirname(__file__), '..', 'src', 'languages', 'template.json'
    )
    with open(template_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_language_file(lang_code, lang_name):
    """Create a new language file interactively."""
    template = load_template()

    print(f"\nCreating language file for {lang_name} ({lang_code})")
    print("=" * 60)
    print("\nPlease provide translations for the following Python keywords and builtins.")
    print("Press Enter to use the English keyword as-is (for words like 'lambda').\n")

    lang_data = {
        "keywords": {},
        "builtins": {}
    }

    # Translate keywords
    print("\n=== KEYWORDS ===\n")
    for keyword in template['keywords']:
        while True:
            translation = input(f"{keyword:15} -> ").strip()
            if not translation:
                translation = keyword

            # Validate that translation is a valid Python identifier
            if translation.isidentifier() or translation in ['True', 'False', 'None']:
                lang_data['keywords'][keyword] = translation
                break
            else:
                print(f"     '{translation}' is not a valid Python identifier. Try again.")

    # Translate builtins
    print("\n=== BUILT-IN FUNCTIONS ===\n")
    for builtin in template['builtins']:
        while True:
            translation = input(f"{builtin:15} -> ").strip()
            if not translation:
                translation = builtin

            # Validate that translation is a valid Python identifier
            if translation.isidentifier():
                lang_data['builtins'][builtin] = translation
                break
            else:
                print(f"     '{translation}' is not a valid Python identifier. Try again.")

    # Save the language file
    output_path = os.path.join(
        os.path.dirname(__file__), '..', 'src', 'languages', f'{lang_code}.json'
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(lang_data, f, indent=2, ensure_ascii=False)

    print(f"\n Language file created successfully: {output_path}")
    print(f"\nYou can now use it with:")
    print(f"  multilang-python --lang {lang_code} your_file.py")

    return output_path

def main():
    """Main entry point."""
    print("=" * 60)
    print("  multilang-python: Add New Language")
    print("=" * 60)

    # Get language information
    lang_code = input("\nEnter language code (e.g., 'fr', 'es', 'de'): ").strip().lower()

    if not lang_code:
        print("L Language code cannot be empty.")
        sys.exit(1)

    if not lang_code.isalnum():
        print("L Language code must be alphanumeric.")
        sys.exit(1)

    # Check if language already exists
    lang_file = os.path.join(
        os.path.dirname(__file__), '..', 'src', 'languages', f'{lang_code}.json'
    )

    if os.path.exists(lang_file):
        overwrite = input(f"   Language '{lang_code}' already exists. Overwrite? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("Cancelled.")
            sys.exit(0)

    lang_name = input("Enter language name (e.g., 'French', 'Spanish'): ").strip()

    if not lang_name:
        print("L Language name cannot be empty.")
        sys.exit(1)

    # Create the language file
    try:
        output_path = create_language_file(lang_code, lang_name)

        # Validate the created file
        print("\n= Validating language file...")
        validate_script = os.path.join(os.path.dirname(__file__), '..', 'src', 'languages', 'validate_lang.py')

        if os.path.exists(validate_script):
            import subprocess
            result = subprocess.run([sys.executable, validate_script, output_path], capture_output=True, text=True)
            if result.returncode == 0:
                print(" Validation passed!")
            else:
                print(f"   Validation warnings:\n{result.stdout}")

    except Exception as e:
        print(f"\nL Error creating language file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

import json
import os
from .errors import ValidationError


class LanguageValidator:
    def __init__(self, schema_file=None):
        """Initialize with an optional schema file."""
        if schema_file is None:
            lang_dir = os.path.join(os.path.dirname(__file__), '..')
            schema_file = os.path.join(lang_dir, 'languages', 'schema.json')
        with open(schema_file, 'r', encoding='utf-8') as f:
            self.schema = json.load(f)

    def validate(self, lang_data):
        """Validate language JSON data against schema."""
        required_sections = self.schema.get('required_sections', [])
        for section in required_sections:
            if section not in lang_data:
                msg = f"Missing required section: {section}"
                raise ValidationError(msg)
            if not isinstance(lang_data[section], dict):
                msg = f"Section {section} must be a dictionary"
                raise ValidationError(msg)
            if not lang_data[section]:
                msg = f"Section {section} cannot be empty"
                raise ValidationError(msg)

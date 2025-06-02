import re
import os
import json
from .cache import TranslationCache
from .errors import TranspilerError, LanguageNotFoundError

class Transpiler:
    def __init__(self, lang_code=None, lang_file=None):
        """Initialize with a language code or file."""
        self.cache = TranslationCache()
        if lang_file:
            self.lang_file = lang_file
        elif lang_code:
            self.lang_file = os.path.join(os.path.dirname(__file__), '..', 'languages', f'{lang_code}.json')
        else:
            raise TranspilerError("Language code or file must be provided.")
        if not os.path.exists(self.lang_file):
            raise LanguageNotFoundError(f"Language file {self.lang_file} not found.")
        with open(self.lang_file, 'r', encoding='utf-8') as f:
            self.translations = json.load(f)

    @staticmethod
    def get_language_from_header(code):
        """Extract language code from file header."""
        match = re.match(r'#\s*multilang-python:\s*(\w+)\s*\n', code, re.IGNORECASE)
        return match.group(1) if match else None

    def translate(self, code):
        """Translate code to standard Python."""
        # Check cache first
        cached_result = self.cache.get(code)
        if cached_result:
            return cached_result

        translated = code
        # Remove the header if present
        translated = re.sub(r'#\s*multilang-python:\s*\w+\s*\n', '', translated, 1)

        # Translate keywords and builtins
        patterns = {
            key: re.compile(r'\b' + re.escape(value) + r'\b')
            for category in ['keywords', 'builtins']
            for key, value in self.translations.get(category, {}).items()
        }
        for key, pattern in patterns.items():
            translated = pattern.sub(key, translated)

        # Cache the result
        self.cache.set(code, translated)
        return translated
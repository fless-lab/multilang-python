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
            lang_dir = os.path.join(os.path.dirname(__file__), '..')
            self.lang_file = os.path.join(lang_dir, 'languages',
                                          f'{lang_code}.json')
        else:
            raise TranspilerError("Language code or file must be provided.")
        if not os.path.exists(self.lang_file):
            msg = f"Language file {self.lang_file} not found."
            raise LanguageNotFoundError(msg)
        with open(self.lang_file, 'r', encoding='utf-8') as f:
            self.translations = json.load(f)

    @staticmethod
    def get_language_from_header(code):
        """Extract language code from file header."""
        pattern = r'#\s*multilang-python:\s*(\w+)\s*\n'
        match = re.match(pattern, code, re.IGNORECASE)
        return match.group(1) if match else None

    def translate(self, code):
        """Translate code to standard Python."""
        # Check cache first
        cached_result = self.cache.get(code)
        if cached_result:
            return cached_result

        translated = code
        # Remove the header if present
        header_pattern = r'#\s*multilang-python:\s*\w+\s*\n'
        translated = re.sub(header_pattern, '', translated, 1)

        # Extract and protect string literals and comments
        protected_items = []
        item_counter = [0]

        def protect_item(match):
            """Replace string/comment with placeholder."""
            placeholder = f"__PROTECTED_ITEM_{item_counter[0]}__"
            protected_items.append((placeholder, match.group(0)))
            item_counter[0] += 1
            return placeholder

        # Protect triple-quoted strings first
        triple_pattern = r'"""[\s\S]*?"""|' + "'''[\\s\\S]*?'''"
        translated = re.sub(triple_pattern, protect_item, translated)
        # Then protect regular strings
        string_pattern = (r'"(?:[^"\\]|\\.)*"|' + r"'(?:[^'\\]|\\.)*'")
        translated = re.sub(string_pattern, protect_item, translated)
        # Protect comments (but not the multilang-python header)
        comment_pattern = r'(?<!multilang-python:)#[^\n]*'
        translated = re.sub(comment_pattern, protect_item, translated)

        # Translate keywords and builtins
        # Format: {native_word: python_word}
        # We search for native_word and replace with python_word
        patterns = {
            python_word: re.compile(r'\b' + re.escape(native_word) + r'\b')
            for category in ['keywords', 'builtins']
            for native_word, python_word in (
                self.translations.get(category, {}).items()
            )
        }
        for python_word, pattern in patterns.items():
            translated = pattern.sub(python_word, translated)

        # Restore protected items (strings and comments)
        for placeholder, original_item in reversed(protected_items):
            translated = translated.replace(placeholder, original_item)

        # Cache the result
        self.cache.set(code, translated)
        return translated

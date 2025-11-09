import os
import sys
import pytest
from multilang_python.core.transpiler import Transpiler
from multilang_python.core.errors import TranspilerError, LanguageNotFoundError


class TestBasicTranspilation:
    """Test basic transpilation functionality."""

    def test_transpiler_french(self):
        """Test translation from French to standard Python."""
        code = """# multilang-python: fr
fonction saluer(nom):
    afficher("Bonjour, " + nom)

saluer("Monde")
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        expected = """def saluer(nom):
    print("Bonjour, " + nom)

saluer("Monde")
"""
        assert translated.strip() == expected.strip()

    def test_transpiler_spanish(self):
        """Test translation from Spanish to standard Python."""
        code = """# multilang-python: es
funcion saludar(nombre):
    mostrar("Hola, " + nombre)

saludar("Mundo")
"""
        trans = Transpiler(lang_code="es")
        translated = trans.translate(code)
        expected = """def saludar(nombre):
    print("Hola, " + nombre)

saludar("Mundo")
"""
        assert translated.strip() == expected.strip()

    def test_transpiler_german(self):
        """Test translation from German to standard Python."""
        code = """# multilang-python: de
funktion gruessen(name):
    drucken("Hallo, " + name)

gruessen("Welt")
"""
        trans = Transpiler(lang_code="de")
        translated = trans.translate(code)
        assert "def gruessen(name):" in translated
        assert 'print("Hallo, " + name)' in translated

    def test_all_languages_exist(self):
        """Test that all language files can be loaded."""
        languages = ["fr", "es", "de", "pt", "it", "ar", "zh"]
        for lang in languages:
            trans = Transpiler(lang_code=lang)
            assert trans.translations is not None
            assert "keywords" in trans.translations
            assert "builtins" in trans.translations


class TestKeywords:
    """Test keyword translation."""

    def test_control_flow_keywords_french(self):
        """Test if/else/elif in French."""
        code = """# multilang-python: fr
si x > 0:
    afficher("positif")
sinon_si x < 0:
    afficher("négatif")
sinon:
    afficher("zéro")
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        assert "if x > 0:" in translated
        assert "elif x < 0:" in translated
        assert "else:" in translated

    def test_loop_keywords_french(self):
        """Test for/while loops in French."""
        code = """# multilang-python: fr
pour i dans intervalle(10):
    afficher(i)

tant_que Vrai:
    arreter
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        assert "for i in range(10):" in translated
        assert "while True:" in translated
        assert "break" in translated

    def test_function_and_class_french(self):
        """Test function and class definitions in French."""
        code = """# multilang-python: fr
classe Animal:
    fonction __init__(soi, nom):
        soi.nom = nom
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        assert "class Animal:" in translated
        assert "def __init__(soi, nom):" in translated

    def test_exception_handling_french(self):
        """Test try/except/finally in French."""
        code = """# multilang-python: fr
essayer:
    x = 1 / 0
sauf ZeroDivisionError comme e:
    afficher("Erreur!")
finalement:
    afficher("Terminé")
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        assert "try:" in translated
        assert "except ZeroDivisionError as e:" in translated
        assert "finally:" in translated

    def test_async_await_keywords(self):
        """Test async/await keywords."""
        code = """# multilang-python: fr
asynchrone fonction fetch():
    attendre quelque_chose()
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        assert "async def fetch():" in translated
        assert "await quelque_chose()" in translated


class TestBuiltinFunctions:
    """Test built-in function translation."""

    def test_common_builtins_french(self):
        """Test common built-in functions in French."""
        code = """# multilang-python: fr
longueur([1, 2, 3])
trier([3, 1, 2])
enumerer(["a", "b"])
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        assert "len([1, 2, 3])" in translated
        assert "sorted([3, 1, 2])" in translated
        assert 'enumerate(["a", "b"])' in translated

    def test_type_conversion_french(self):
        """Test type conversion functions."""
        code = """# multilang-python: fr
entier("42")
flottant("3.14")
chaîne(123)
booleen(1)
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        assert 'int("42")' in translated
        assert 'float("3.14")' in translated
        assert "str(123)" in translated
        assert "bool(1)" in translated


class TestStringProtection:
    """Test that strings are protected from translation."""

    def test_keywords_in_strings_not_translated(self):
        """Keywords inside strings should not be translated."""
        code = """# multilang-python: fr
afficher("si vous voulez pour tester")
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        # "si" and "pour" inside the string should NOT be translated
        assert 'print("si vous voulez pour tester")' in translated
        assert "if" not in translated or translated.count("print") == 1

    def test_triple_quoted_strings_protected(self):
        """Triple-quoted strings should be protected."""
        code = '''# multilang-python: fr
texte = """
pour chaque si dans la liste
tant_que nous testons
"""
afficher(texte)
'''
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        # Content inside triple quotes should not be translated
        assert 'pour chaque si dans la liste' in translated
        assert 'tant_que nous testons' in translated

    def test_f_strings_protected(self):
        """F-strings should be protected."""
        code = """# multilang-python: fr
nom = "Alice"
afficher(f"Bonjour {nom}, si vous voulez")
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        # "si" inside f-string should not be translated
        assert 'print(f"Bonjour {nom}, si vous voulez")' in translated


class TestCommentProtection:
    """Test that comments are protected from translation."""

    def test_comments_not_translated(self):
        """Keywords in comments should not be translated."""
        code = """# multilang-python: fr
# Ceci est un commentaire avec si et pour
afficher("test")  # Un autre commentaire avec tant_que
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)
        # Comments should remain intact
        assert "# Ceci est un commentaire avec si et pour" in translated
        assert "# Un autre commentaire avec tant_que" in translated


class TestEdgeCases:
    """Test edge cases and special scenarios."""

    def test_language_detection_from_header(self):
        """Test automatic language detection from header."""
        code = "# multilang-python: es\nmostrar('Hola')"
        detected = Transpiler.get_language_from_header(code)
        assert detected == "es"

    def test_missing_language_file_raises_error(self):
        """Test that missing language file raises error."""
        with pytest.raises(LanguageNotFoundError):
            Transpiler(lang_code="nonexistent")

    def test_no_language_code_or_file_raises_error(self):
        """Test that missing language code/file raises error."""
        with pytest.raises(TranspilerError):
            Transpiler()

    def test_cache_functionality(self):
        """Test that caching works correctly."""
        code = "# multilang-python: fr\nafficher('test')"
        trans = Transpiler(lang_code="fr")

        # First translation
        result1 = trans.translate(code)

        # Second translation (should use cache)
        result2 = trans.translate(code)

        assert result1 == result2
        # Verify cache was used (same object from cache)
        assert trans.cache.get(code) is not None

    def test_mixed_keywords_and_builtins(self):
        """Test code with both keywords and builtins."""
        code = """# multilang-python: fr
fonction calculer(nombres):
    si longueur(nombres) == 0:
        retourner 0
    retourner somme(nombres) / longueur(nombres)

pour i dans intervalle(10):
    afficher(calculer([i, i+1, i+2]))
"""
        trans = Transpiler(lang_code="fr")
        translated = trans.translate(code)

        assert "def calculer(nombres):" in translated
        assert "if len(nombres) == 0:" in translated
        assert "return 0" in translated
        assert "return sum(nombres) / len(nombres)" in translated
        assert "for i in range(10):" in translated
        assert "print(calculer([i, i+1, i+2]))" in translated


class TestAllLanguages:
    """Test basic functionality for all supported languages."""

    @pytest.mark.parametrize("lang_code", ["fr", "es", "de", "pt", "it"])
    def test_basic_program_all_languages(self, lang_code):
        """Test a basic program translates correctly for all languages."""
        trans = Transpiler(lang_code=lang_code)

        # Get print keyword from language file (format: {native: python})
        # Find the native word that maps to "print"
        print_keyword = [k for k, v in trans.translations["builtins"].items() if v == "print"][0]

        code = f"""# multilang-python: {lang_code}
{print_keyword}("Hello World")
"""
        translated = trans.translate(code)
        assert 'print("Hello World")' in translated

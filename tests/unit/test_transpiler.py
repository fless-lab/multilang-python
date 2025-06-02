import os
import sys
import pytest
from multilang_python.core.transpiler import Transpiler

def test_transpiler_french():
    """Test translation from French to standard Python."""
    code = """# multilang-python: fr
définir saluer(nom):
    afficher("Bonjour, " + nom)

saluer("Monde")
"""
    trans = Transpiler(lang_code="fr")
    translated = trans.translate(code)
    expected = """def greet(name):
    print("Hello, " + name)

greet("World")
"""
    assert translated.strip() == expected.strip()

def test_missing_header():
    """Test that a missing header raises an error."""
    code = """définir saluer(nom):
    afficher("Bonjour, " + nom)
"""
    with pytest.raises(Exception):
        trans = Transpiler()
        trans.translate(code)
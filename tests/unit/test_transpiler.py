import os
import sys
import pytest
from multilang_python.core.transpiler import Transpiler

def test_transpiler_french():
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

def test_transpiler_spanish():
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

def test_missing_header():
    """Test that a missing header raises an error."""
    code = """fonction saluer(nom):
    afficher("Bonjour, " + nom)
"""
    with pytest.raises(Exception):
        trans = Transpiler()
        trans.translate(code)
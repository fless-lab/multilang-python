# Multilang-Python

[![Tests](https://github.com/fless-lab/multilang-python/actions/workflows/test.yml/badge.svg)](https://github.com/fless-lab/multilang-python/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

**multilang-python** is an open-source transpiler that enables Python code to be written in any native language. Write Python using keywords and built-in functions in your mother tongue (e.g., French `fonction` → `def`, `afficher` → `print`) and execute it like standard Python. Perfect for education, accessibility, and international communities.

## Features

- **7 Languages Supported**: French, Spanish, German, Portuguese, Italian, Arabic (transliterated), Chinese (Pinyin)
- **Zero Dependencies**: Uses only Python standard library
- **Easy to Use**: Simple language header, instant execution
- **Extensible**: Add new languages via JSON files
- **High Performance**: Optimized with intelligent caching
- **Robust**: Protects strings and comments from translation
- **Well-Tested**: Comprehensive test suite with 25+ tests
- **Educational**: Perfect for teaching Python to non-English speakers

## Supported Languages

| Language | Code | Example Keyword | Status |
|----------|------|-----------------|--------|
| French | `fr` | `fonction`, `afficher` | ✅ Complete |
| Spanish | `es` | `funcion`, `mostrar` | ✅ Complete |
| German | `de` | `funktion`, `drucken` | ✅ Complete |
| Portuguese | `pt` | `funcao`, `imprimir` | ✅ Complete |
| Italian | `it` | `funzione`, `stampa` | ✅ Complete |
| Arabic (Latin) | `ar` | `tareef`, `taba` | ✅ Complete |
| Chinese (Pinyin) | `zh` | `dingyi`, `dayin` | ✅ Complete |

**Each language includes:**
- ✅ All 35 Python keywords
- ✅ 60+ built-in functions
- ✅ Full test coverage

## Installation

### Prerequisites
- Python 3.7+ (3.10+ recommended)
- pip (included with Python)

### Install via pip
```bash
pip install multilang-python
```

### Install from source (for development)
```bash
git clone https://github.com/fless-lab/multilang-python.git
cd multilang-python
pip install -e .
```

### Verify installation
```bash
multilang-python --version
# Output: multilang-python 0.1.0
```

## Quick Start

### 1. Write code in your language

**French example** (`hello.py`):
```python
# multilang-python: fr

fonction saluer(nom):
    """Affiche un message de bienvenue."""
    afficher(f"Bonjour, {nom}!")
    afficher("Bienvenue dans multilang-python!")

si __name__ == "__main__":
    nom = saisir("Quel est votre nom? ")
    saluer(nom)
```

**Spanish example** (`hello.py`):
```python
# multilang-python: es

funcion saludar(nombre):
    """Muestra un mensaje de bienvenida."""
    mostrar(f"¡Hola, {nombre}!")
    mostrar("¡Bienvenido a multilang-python!")

si __name__ == "__main__":
    nombre = entrada("¿Cuál es tu nombre? ")
    saludar(nombre)
```

### 2. Run your code

```bash
# Translate and execute
multilang-python hello.py

# Just translate (save to file)
multilang-python hello.py --output hello_translated.py

# Specify language explicitly
multilang-python hello.py --lang fr
```

### 3. See the magic

Your native-language code runs just like standard Python!

## More Examples

### French Calculator
```python
# multilang-python: fr

fonction calculer(a, b, operation):
    si operation == "+":
        retourner a + b
    sinon_si operation == "-":
        retourner a - b
    sinon_si operation == "*":
        retourner a * b
    sinon_si operation == "/":
        si b != 0:
            retourner a / b
        sinon:
            retourner "Erreur: division par zéro"

# Utilisation
resultat = calculer(10, 5, "+")
afficher(f"Résultat: {resultat}")
```

### Spanish Data Processing
```python
# multilang-python: es

funcion procesar_lista(numeros):
    # Filtrer les nombres pairs
    pares = filtrar(lambda x: x % 2 == 0, numeros)

    # Calculer statistiques
    total = suma(pares)
    promedio = total / longitud(pares) si longitud(pares) > 0 sino 0

    retornar {
        "pares": lista(pares),
        "total": total,
        "promedio": promedio
    }

# Utilisation
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = procesar_lista(numeros)
mostrar(resultado)
```

## 🛠️ Command Line Interface

```bash
# Basic usage
multilang-python <file.py>

# Save translated output
multilang-python <file.py> --output <output.py>

# Specify language (overrides header)
multilang-python <file.py> --lang fr

# List available languages
multilang-python --list-langs

# Show version
multilang-python --version

# Run as Python module
python -m multilang_python <file.py>
```

## Developer Tools

### Validate language files
```bash
python scripts/validate_all.py
```

### Add a new language
```bash
python scripts/add_language.py
```

### Watch mode (auto-translate on save)
```bash
python scripts/watch.py examples/french/*.py --output translated/
```

### Run tests
```bash
pytest tests/ -v
pytest tests/unit/test_transpiler.py -v
```

## How It Works

1. **Parse**: Reads your source file and detects the language from the header
2. **Protect**: Preserves strings, comments, and docstrings from translation
3. **Translate**: Converts native keywords/builtins to Python equivalents using regex
4. **Execute**: Runs the translated code with the Python interpreter

**Example Translation:**

```python
# Input (French)
fonction calculer(x):
    retourner x * 2

# Output (Python)
def calculer(x):
    return x * 2
```

## Key Features Explained

### String & Comment Protection
Multilang-python intelligently protects string literals and comments:

```python
# multilang-python: fr

# This comment with 'si' and 'pour' stays unchanged
afficher("This string with 'pour' stays unchanged")

pour i dans intervalle(10):
    afficher(i)  # This works correctly!
```

### Comprehensive Language Support
Every language includes:
- **35 keywords**: `def`, `if`, `else`, `for`, `while`, `class`, `try`, `async`, `await`, etc.
- **60+ built-ins**: `print`, `len`, `range`, `input`, `enumerate`, `isinstance`, etc.
- **Type conversions**: `int`, `float`, `str`, `bool`, `list`, `dict`, etc.
- **Advanced functions**: `map`, `filter`, `zip`, `sorted`, `lambda`, etc.

### Standard Library Wrappers (Optional)
Use native-language wrappers for Python's standard library:

```python
# multilang-python: fr
depuis multilang_python.stdlib.fr importer systeme, json

# Use French names for stdlib functions!
si systeme.chemin_existe("fichier.txt"):
    donnees = json.charger('{"nom": "test"}')
    afficher(donnees)
```

**Available wrappers:**
- `systeme` → `os` module (file/directory operations)
- `json` → `json` module (JSON parsing)
- `sys` → `sys` module (system operations)

See [STDLIB_WRAPPERS.md](docs/STDLIB_WRAPPERS.md) for complete documentation.

### Performance Optimization
- **Caching**: Translated code is cached for instant re-execution
- **Efficient regex**: Optimized pattern matching
- **Minimal overhead**: Translation adds negligible runtime cost

## Contributing

We welcome contributions! Here's how to add a new language:

### Option 1: Interactive Tool
```bash
python scripts/add_language.py
# Follow the prompts to add your language
```

### Option 2: Manual Creation
1. Create `src/languages/your_lang.json`:
```json
{
  "keywords": {
    "your_def": "def",
    "your_if": "if",
    ...
  },
  "builtins": {
    "your_print": "print",
    "your_len": "len",
    ...
  }
}
```

2. Test your language:
```bash
python scripts/validate_all.py
pytest tests/unit/test_transpiler.py
```

3. Create examples in `examples/your_lang/`

4. Submit a pull request!

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Built for educators, students, and developers worldwide
- Inspired by the need for programming accessibility
- Community-driven with ❤️

## Support & Community

- **Issues**: [GitHub Issues](https://github.com/fless-lab/multilang-python/issues)
- **Discussions**: [GitHub Discussions](https://github.com/fless-lab/multilang-python/discussions)
- **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## Roadmap

- [ ] More languages (Russian, Japanese, Hindi, etc.)
- [ ] IDE plugins (VSCode, PyCharm)
- [ ] Error messages in native languages
- [ ] Standard library translation (comprehensive support)
- [ ] Interactive web playground
- [ ] VS Code syntax highlighting

---

**Made with ❤️ for the global Python community**

If you find this project useful, please ⭐ star it on GitHub!

# Multilang-Python

[![Tests](https://github.com/<your-username>/multilang-python/actions/workflows/test.yml/badge.svg)](https://github.com/<your-username>/multilang-python/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**multilang-python** is an open-source transpileur that enables Python code to be written in any native language by translating localized keywords and built-in functions (e.g., French `définir` to `def`, `afficher` to `print`) into standard Python. Designed for accessibility, it empowers non-English-speaking communities, particularly in education, to code in their mother tongue. Built with a modular, extensible, and scalable architecture using only the Python standard library, it supports all Python keywords and built-ins.

## Features

- **Multilingual Coding**: Write Python in your native language (e.g., French, Spanish) using a simple file header.
- **No Dependencies**: Uses only the Python standard library.
- **Easy Installation**: Install via `pip install multilang-python`.
- **Extensible**: Add new languages via JSON files (see [CONTRIBUTING.md](docs/CONTRIBUTING.md)).
- **Scalable**: Optimized with caching for large projects.
- **Collaborative**: Open-source with clear contribution guidelines.

## Installation

### Prerequisites
- Python 3.6+ (e.g., 3.10 recommended).
- pip (included with Python).

### Steps
Install via pip:
```bash
pip install multilang-python
```
Verify:
```bash
multilang-python --version
```
**Output**:
```
multilang-python 0.1.0
```

See [USER_GUIDE.md](docs/USER_GUIDE.md) for detailed setup.

## Usage

### Write Code
Create a `.py` file with a language header, e.g., `hello_world.py`:
```python
# multilang-python: fr

définir saluer(nom):
    afficher("Bonjour, " + nom)

saluer("Monde")
```

### Run Code
```bash
multilang-python hello_world.py
```
**Output**:
```
Translated code:
def greet(name):
    print("Hello, " + name)
greet("World")
Hello, World
```

### Save Translated Code
```bash
multilang-python hello_world.py --output translated.py
```

### List Available Languages
```bash
multilang-python --list-langs
```
**Output**:
```
Available languages: ['fr', 'es']
```

See [USER_GUIDE.md](docs/USER_GUIDE.md) for more examples.

## Project Structure

- `src/multilang_python/core/`: Transpileur, parser, and validator logic.
- `src/multilang_python/languages/`: JSON translation files.
- `src/multilang_python/interfaces/`: CLI and plugin interfaces.
- `tests/`: Unit, integration, and benchmark tests.
- `examples/`: Language-specific scripts.
- `docs/`: Documentation.
- `scripts/`: Contributor utilities.

See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.

## Contributing

We welcome contributions! To get started:
1. Read [CONTRIBUTING.md](docs/CONTRIBUTING.md).
2. Add languages, fix bugs, or improve documentation.
3. Submit a pull request.

## License

[MIT License](LICENSE)

## Community

- **Issues**: Report bugs or suggest features on GitHub.
- **Discussions**: Join GitHub Discussions for questions.
- **Code of Conduct**: See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Thank you for supporting **multilang-python** to make programming inclusive!
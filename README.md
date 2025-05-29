# Multilang-Python

[![Tests](https://github.com/fless-lab/multilang-python/actions/workflows/test.yml/badge.svg)](https://github.com/fless-lab/multilang-python/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**multilang-python** is an open-source transpileur that enables Python code to be written in any native language by translating localized keywords and built-in functions (e.g., French `définir` to `def`, `afficher` to `print`) into standard Python. Designed for accessibility, it empowers non-English-speaking communities, particularly in education, to code in their mother tongue. Built with a modular, extensible, and scalable architecture using only the Python standard library, it supports all Python keywords and built-ins, with easy language additions via JSON files.

## Features

- **Multilingual Coding**: Write Python in your native language (e.g., French, Spanish).
- **No Dependencies**: Uses only the Python standard library for portability.
- **Extensible**: Add new languages via JSON files with `scripts/add_language.py`.
- **Scalable**: Optimized with caching for large projects.
- **Collaborative**: Open-source with clear contribution guidelines.
- **Educational**: Ideal for teaching Python in non-English-speaking regions.

## Installation

### Prerequisites
- Python 3.6+ (e.g., 3.10 recommended).
- Git.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/fless-lab/multilang-python.git
   cd multilang-python
   ```
2. No dependencies required (uses standard library).
3. (Optional) Set up a global command:
   ```bash
   chmod +x multilang-python
   sudo mv multilang-python /usr/local/bin/
   ```

See [USER_GUIDE.md](docs/USER_GUIDE.md) for detailed setup.

## Usage

### Run a Script
Transpile and execute a script in a native language:
```bash
python3 -m multilang_python --lang fr examples/french/hello_world.py
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
python3 -m multilang_python --lang fr examples/french/calculator.py --output translated.py
```

### List Available Languages
```bash
python3 -m multilang_python --list-langs
```
**Output**:
```
Available languages: ['fr', 'es']
```

### Add a New Language
```bash
python3 scripts/add_language.py
```
Follow prompts to create a new language file (e.g., `src/languages/es.json`).

### Example
French script (`examples/french/hello_world.py`):
```python
définir saluer(nom):
    afficher("Bonjour, " + nom)

saluer("Monde")
```

See [USER_GUIDE.md](docs/USER_GUIDE.md) for more examples.

## Project Structure

- `src/core/`: Transpileur, parser, and validator logic.
- `src/languages/`: JSON translation files.
- `src/interfaces/`: CLI and plugin interfaces.
- `tests/`: Unit, integration, and benchmark tests.
- `examples/`: Language-specific scripts.
- `docs/`: Documentation.
- `scripts/`: Contributor utilities.

See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.

## Contributing

We welcome contributions! To get started:
1. Read [CONTRIBUTING.md](docs/CONTRIBUTING.md).
2. Fork the repository and create a branch.
3. Add features, fix bugs, or improve documentation.
4. Write tests and ensure CI/CD passes.
5. Submit a pull request.

Common contributions:
- Add a new language with `scripts/add_language.py`.
- Write tests in `tests/`.
- Enhance documentation in `docs/`.
- Develop IDE plugins in `src/interfaces/plugins/`.

## License

[MIT License](LICENSE)

## Community

- **Issues**: Report bugs or suggest features on GitHub.
- **Discussions**: Join GitHub Discussions for questions or ideas.
- **Code of Conduct**: See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Thank you for supporting **multilang-python** to make programming inclusive!
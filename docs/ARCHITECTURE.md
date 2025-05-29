# Multilang-Python Architecture

## Introduction

`multilang-python` is an open-source transpileur that enables Python code to be written in any native language, translating localized keywords and built-in functions (e.g., French `définir` to `def`, `afficher` to `print`) into standard Python for execution. Designed for accessibility, it empowers non-English-speaking communities, particularly in education, to code in their mother tongue. This document outlines the project’s architecture, directory structure, and component responsibilities to guide contributors in understanding and enhancing the project.

The architecture is **modular**, **extensible**, **scalable**, and **collaborative**, built with only the Python standard library to ensure portability. It supports all Python keywords and built-in functions, with a JSON-based system for adding languages, and is optimized for performance, maintainability, and open-source contributions.

## Design Principles

- **Modularity**: Components are isolated (e.g., transpileur, parser, CLI) for independent development and testing.
- **Extensibility**: New languages, parsers, or interfaces (e.g., IDE plugins) can be added without modifying core logic.
- **Scalability**: Efficient caching and parsing handle large codebases and numerous languages.
- **Collaborative**: Comprehensive documentation, CI/CD pipelines, and contribution templates support open-source workflows.
- **Maintainability**: Clean code, robust tests, and linting ensure long-term quality.
- **Portability**: No external dependencies ensure easy setup across platforms.
- **Future-Proofing**: Designed for enhancements like advanced parsing, C++ migration, or web APIs.
- **Security**: Custom error handling and a security policy protect users and contributors.

## Repository Structure

Below is the complete directory structure with descriptions of each component’s purpose.

```
multilang-python/
├── src/
│   ├── core/
│   │   ├── __init__.py           # Module initialization
│   │   ├── transpiler.py         # Core transpileur logic
│   │   ├── parser.py             # Code parser (regex-based, extensible)
│   │   ├── validator.py          # Language JSON validation
│   │   ├── cache.py              # Translation caching
│   │   ├── errors.py             # Custom exceptions
│   │   └── utils.py              # Shared utilities
│   ├── languages/
│   │   ├── fr.json               # French translations
│   │   ├── es.json               # Spanish translations
│   │   ├── template.json         # Template for new languages
│   │   ├── schema.json           # JSON schema for validation
│   │   └── validate_lang.py      # Validates a single JSON file
│   ├── interfaces/
│   │   ├── __init__.py
│   │   ├── cli.py                # Command-line interface
│   │   ├── api.py                # Placeholder for REST API
│   │   └── plugins/
│   │       ├── __init__.py
│   │       ├── vscode/
│   │       │   ├── extension.py  # VSCode extension logic
│   │       │   └── package.json  # VSCode extension config
│   │       └── pycharm/
│   │           ├── plugin.py     # PyCharm plugin placeholder
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py           # Global configuration
│   │   └── logging.py            # Logging setup
│   └── __main__.py               # Entry point (python -m multilang_python)
├── tests/
│   ├── unit/
│   │   ├── test_transpiler.py   # Transpileur unit tests
│   │   ├── test_parser.py       # Parser unit tests
│   │   ├── test_validator.py    # Validator unit tests
│   │   ├── test_cache.py        # Cache unit tests
│   │   └── test_utils.py        # Utilities unit tests
│   ├── integration/
│   │   ├── test_french.py       # French integration tests
│   │   ├── test_spanish.py      # Spanish integration tests
│   │   └── test_multilang.py    # Cross-language tests
│   ├── benchmarks/
│   │   ├── benchmark_transpiler.py  # Transpileur performance
│   │   └── benchmark_parser.py      # Parser performance
│   └── data/
│       ├── french/
│       │   ├── valid.py         # Valid French sample
│       │   └── invalid.py       # Invalid French sample
│       ├── spanish/
│       │   ├── valid.py         # Valid Spanish sample
│       └── malformed/
│           ├── syntax_error.py  # Malformed code for testing
├── examples/
│   ├── french/
│   │   ├── hello_world.py       # Simple French example
│   │   ├── calculator.py        # Advanced French example
│   │   └── data_processing.py   # Complex French example
│   ├── spanish/
│   │   ├── hello_world.py       # Simple Spanish example
│   └── other/
│       ├── placeholder.md       # Guide for new language examples
├── scripts/
│   ├── add_language.py          # Creates new language JSON
│   ├── validate_all.py          # Validates all language files
│   ├── generate_docs.py         # Generates API documentation
│   ├── setup_dev.py             # Sets up dev environment
│   └── watch.py                 # Auto-translates modified files
├── docs/
│   ├── README.md                # Project overview and setup
│   ├── USER_GUIDE.md            # User guide
│   ├── CONTRIBUTING.md          # Contribution guidelines
│   ├── ARCHITECTURE.md          # This file
│   ├── API.md                   # API documentation
│   ├── CHANGELOG.md             # Version history
│   ├── FAQ.md                   # Frequently asked questions
│   └── RELEASE.md               # Release process
├── .github/
│   ├── workflows/
│   │   ├── test.yml             # Unit and integration tests
│   │   ├── lint.yml             # Linting (flake8)
│   │   ├── benchmark.yml        # Performance benchmarks
│   │   ├── docs.yml             # Documentation validation
│   │   └── release.yml          # Automated releases
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md        # Bug report template
│   │   ├── feature_request.md   # Feature request template
│   │   └── language_request.md  # New language template
│   ├── PULL_REQUEST_TEMPLATE.md # PR template
│   └── dependabot.yml           # Future dependency updates
├── config/
│   ├── flake8.ini               # Linting rules
│   ├── pytest.ini               # Test configuration
│   ├── logging.yaml             # Logging setup
├── tools/
│   ├── release.sh               # Release automation
│   ├── lint.sh                  # Linting script
│   ├── format.sh                # Code formatting (black, isort)
├── requirements/
│   ├── dev.txt                  # Optional dev dependencies
│   ├── test.txt                 # Test dependencies
│   ├── docs.txt                 # Documentation dependencies
├── requirements.txt              # Empty (standard library only)
├── setup.py                     # pip installation
├── pyproject.toml               # Project metadata
├── MANIFEST.in                  # Distribution files
├── LICENSE                      # MIT license
├── CODE_OF_CONDUCT.md           # Community standards
├── SECURITY.md                  # Security policy
├── .gitignore                   # Ignores artifacts
├── .editorconfig                # Editor consistency
├── multilang-python             # Shell script for CLI
└── Dockerfile                   # Containerization
```

## Component Details

### src/
The core source code, organized for modularity and extensibility.

- **core/**: Core transpileur and supporting logic.
  - `__init__.py`: Marks the directory as a Python module.
  - `transpiler.py`: Translates native-language code to standard Python.
  - `parser.py`: Parses code (currently regex-based, extensible to `ast` or `tokenize`).
  - `validator.py`: Validates language JSON files for completeness.
  - `cache.py`: Manages translation caching for performance.
  - `errors.py`: Defines custom exceptions (e.g., `InvalidLanguageError`).
  - `utils.py`: Shared utilities (e.g., file I/O, logging).
- **languages/**: Stores translation files and validation tools.
  - `fr.json`, `es.json`: Language-specific keyword and built-in translations.
  - `template.json`: Template for creating new language files.
  - `schema.json`: JSON schema for validating language files.
  - `validate_lang.py`: Script to validate a single language file.
- **interfaces/**: User interaction layers.
  - `__init__.py`: Module initialization.
  - `cli.py`: CLI for running the transpileur (e.g., `--lang fr`).
  - `api.py`: Placeholder for a future REST API.
  - `plugins/vscode/`, `plugins/pycharm/`: IDE plugin implementations.
- **config/**: Configuration management.
  - `__init__.py`: Module initialization.
  - `settings.py`: Global settings (e.g., cache size, verbosity).
  - `logging.py`: Configures logging (file, console, levels).
- `__main__.py`: Entry point for `python -m multilang_python`.

### tests/
Comprehensive testing to ensure reliability and quality.

- **unit/**: Tests individual components (e.g., `test_transpiler.py`).
- **integration/**: Tests end-to-end workflows for specific languages.
- **benchmarks/**: Performance tests for scalability.
- **data/**: Sample scripts (valid, invalid, malformed) for testing.

### examples/
Language-specific example scripts to demonstrate usage.

- **french/**, **spanish/**: Sample scripts (e.g., `hello_world.py`).
- **other/**: Placeholder for new languages with contribution instructions.

### scripts/
Utilities for contributors and maintainers.

- `add_language.py`: Interactive script to create language JSON files.
- `validate_all.py`: Validates all language files.
- `generate_docs.py`: Generates API documentation.
- `setup_dev.py`: Sets up development environment.
- `watch.py`: Monitors directories for auto-translation.

### docs/
Documentation for users, contributors, and maintainers.

- `README.md`: Project overview, setup, and quick start.
- `USER_GUIDE.md`: Detailed usage instructions.
- `CONTRIBUTING.md`: How to contribute (e.g., adding languages).
- `ARCHITECTURE.md`: This file.
- `API.md`: CLI and future API documentation.
- `CHANGELOG.md`: Version history.
- `FAQ.md`: Common questions.
- `RELEASE.md`: Release process.

### .github/
GitHub-specific configurations for collaboration.

- **workflows/**: CI/CD pipelines for testing, linting, benchmarks, and releases.
- **ISSUE_TEMPLATE/**: Templates for bugs, features, and language requests.
- **PULL_REQUEST_TEMPLATE.md**: PR submission guidelines.
- **dependabot.yml**: Future dependency management.

### config/
Configuration files for tools.

- `flake8.ini`: Linting rules.
- `pytest.ini`: Test settings.
- `logging.yaml`: Logging configuration.

### tools/
Scripts for development and maintenance.

- `release.sh`: Automates release tagging and publishing.
- `lint.sh`: Runs linting.
- `format.sh`: Applies code formatting.

### requirements/
Dependency management for contributors.

- `dev.txt`, `test.txt`, `docs.txt`: Optional dependencies.
- `requirements.txt`: Empty for CLI usage.

### Root Files
- `setup.py`, `pyproject.toml`: Packaging and metadata.
- `MANIFEST.in`: Includes non-code files in distribution.
- `LICENSE`: MIT license.
- `CODE_OF_CONDUCT.md`: Community guidelines.
- `SECURITY.md`: Security reporting.
- `.gitignore`: Ignores Python artifacts.
- `.editorconfig`: Ensures editor consistency.
- `multilang-python`: Shell script for global CLI.
- `Dockerfile`: Containerizes the project.

## Scalability and Collaboration

- **Scalability**:
  - **Caching**: `cache.py` optimizes repeated translations.
  - **Parser**: `parser.py` supports regex now, with hooks for `ast` or `tokenize`.
  - **Configuration**: `config/` allows tuning (e.g., cache size).
  - **Unicode**: UTF-8 supports non-Latin scripts.
- **Collaboration**:
  - **Documentation**: Extensive guides in `docs/`.
  - **CI/CD**: Automated workflows ensure quality.
  - **Templates**: GitHub issue/PR templates streamline contributions.
  - **Scripts**: `add_language.py` simplifies language additions.
  - **Community**: `CODE_OF_CONDUCT.md` and `SECURITY.md`.

## Contributing

To contribute:
1. Review `CONTRIBUTING.md` for guidelines.
2. Add a language with `scripts/add_language.py`.
3. Write tests in `tests/`.
4. Submit a pull request with clear descriptions.
5. Ensure code passes CI/CD (tests, linting).

See `docs/CONTRIBUTING.md` for details.

## Future Enhancements

- Advanced parsing (`ast` or `tokenize`) in `parser.py`.
- REST API in `interfaces/api.py`.
- IDE plugins (`plugins/vscode/`, `plugins/pycharm/`).
- C++ migration for performance-critical components.
- Support for third-party library translations.
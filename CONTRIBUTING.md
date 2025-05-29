# Contributing to Multilang-Python

Thank you for your interest in contributing to **multilang-python**, an open-source transpileur that enables Python coding in native languages by translating localized keywords and built-ins (e.g., French `définir` to `def`) into standard Python. Your contributions help make programming more accessible to non-English-speaking communities. This guide outlines how to contribute effectively, ensuring a smooth and collaborative experience.

## Code of Conduct

We are committed to a respectful and inclusive community. Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions.

## How to Contribute

Contributions can take many forms, including code, documentation, language translations, bug reports, feature requests, and more. Below are the primary ways to contribute.

### 1. Reporting Bugs

If you find a bug, please submit an issue using the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md). Include:
- A clear description of the issue.
- Steps to reproduce (e.g., sample code, command used).
- Expected and actual behavior.
- Environment details (e.g., Python version, OS).

### 2. Suggesting Features

Propose new features or enhancements via the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md). Provide:
- A detailed description of the feature.
- Use cases and benefits.
- Any potential challenges or alternatives.

### 3. Adding a New Language

To add a new language:
1. Run the `add_language.py` script:
   ```bash
   python3 scripts/add_language.py
   ```
2. Enter the language code (e.g., `es` for Spanish) and translations for each keyword and built-in.
3. Save the generated file (e.g., `src/languages/es.json`).
4. Add example scripts in `examples/<language>/` (e.g., `examples/spanish/hello_world.py`).
5. Write integration tests in `tests/integration/test_<language>.py`.
6. Submit a pull request with your changes.

See `src/languages/template.json` for the required structure and `docs/USER_GUIDE.md` for details.

### 4. Code Contributions

To contribute code (e.g., bug fixes, new features, optimizations):
1. **Fork the Repository**:
   ```bash
   git clone https://github.com/fless-lab/multilang-python.git
   cd multilang-python
   ```
2. **Create a Branch**:
   ```bash
   git checkout -b feature/<your-feature>  # or bugfix/<your-bug>
   ```
3. **Set Up Development Environment**:
   ```bash
   python3 scripts/setup_dev.py
   ```
   This sets up optional dev dependencies (e.g., `pytest`, `flake8`) from `requirements/dev.txt`.
4. **Write Code**:
   - Follow the architecture in `docs/ARCHITECTURE.md`.
   - Adhere to PEP 8, enforced via `flake8` (see `config/flake8.ini`).
   - Add unit tests in `tests/unit/` or integration tests in `tests/integration/`.
5. **Test Locally**:
   ```bash
   python3 -m pytest tests/
   ```
6. **Format Code**:
   ```bash
   ./tools/format.sh
   ```
7. **Commit Changes**:
   Use clear commit messages (e.g., `Add Spanish language support in src/languages/es.json`).
   ```bash
   git commit -m "Your message"
   ```
8. **Submit a Pull Request**:
   - Push to your fork and create a PR using the [PR template](.github/PULL_REQUEST_TEMPLATE.md).
   - Link to relevant issues.
   - Ensure CI/CD pipelines (tests, linting) pass.

### 5. Improving Documentation

Documentation is critical for accessibility. To contribute:
- Update files in `docs/` (e.g., `USER_GUIDE.md`, `API.md`).
- Fix typos, improve clarity, or add examples.
- Run `scripts/generate_docs.py` to update API documentation.
- Submit a PR with your changes.

### 6. Other Contributions

- **Performance Benchmarks**: Add tests in `tests/benchmarks/`.
- **IDE Plugins**: Extend `src/interfaces/plugins/` (e.g., VSCode, PyCharm).
- **Translations**: Translate documentation to other languages.
- **Community Engagement**: Answer questions on GitHub issues or promote the project.

## Development Workflow

- **Branch Naming**: Use `feature/<name>`, `bugfix/<name>`, or `docs/<name>` for clarity.
- **Testing**: All code must include tests. Use `pytest` (see `config/pytest.ini`).
- **Linting**: Run `flake8` via `./tools/lint.sh`.
- **CI/CD**: GitHub Actions (`test.yml`, `lint.yml`) validate PRs. Ensure pipelines pass.
- **Code Review**: PRs require at least one maintainer approval. Address feedback promptly.
- **Releases**: Maintainers handle releases per `docs/RELEASE.md`.

## Project Structure

See [ARCHITECTURE.md](ARCHITECTURE.md) for a detailed breakdown. Key directories:
- `src/core/`: Transpileur, parser, and validator logic.
- `src/languages/`: JSON translation files.
- `src/interfaces/`: CLI and plugin interfaces.
- `tests/`: Unit, integration, and benchmark tests.
- `examples/`: Language-specific sample scripts.
- `docs/`: Comprehensive documentation.
- `scripts/`: Contributor utilities.

## Getting Help

- **Issues**: Search existing issues or create a new one.
- **Discussions**: Use GitHub Discussions for questions or ideas.
- **Contact**: Reach out to maintainers via GitHub.

## License

Contributions are licensed under the [MIT License](LICENSE). By contributing, you agree to this license.

Thank you for helping make **multilang-python** more inclusive and powerful!
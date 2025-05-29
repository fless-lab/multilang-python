# Contributing to Multilang-Python

Thank you for your interest in contributing to **multilang-python**, an open-source transpileur that enables Python coding in native languages by translating localized keywords and built-ins (e.g., French `définir` to `def`) into standard Python. Your contributions help make programming accessible to non-English-speaking communities. This guide outlines how to contribute effectively.

## Code of Conduct

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a respectful and inclusive community.

## How to Contribute

Contributions include code, documentation, language translations, bug reports, and more. Below are the main ways to contribute.

### 1. Reporting Bugs

Submit bugs using the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md). Include:
- Issue description.
- Steps to reproduce (e.g., script with `# multilang-python: fr`).
- Expected vs. actual behavior.
- Environment (Python version, OS).

### 2. Suggesting Features

Propose features via the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md). Provide:
- Feature description.
- Use cases (e.g., new language support).
- Potential challenges.

### 3. Adding a New Language

To add a language:
1. Install the package:
   ```bash
   pip install multilang-python
   ```
2. Clone the repository for development:
   ```bash
   git clone https://github.com/<your-username>/multilang-python.git
   cd multilang-python
   ```
3. Run:
   ```bash
   python3 scripts/add_language.py
   ```
4. Enter the language code (e.g., `es`) and translations.
5. Save the file (e.g., `src/multilang_python/languages/es.json`).
6. Add examples in `examples/<language>/` with headers (e.g., `# multilang-python: es`).
7. Write tests in `tests/integration/test_<language>.py`.
8. Submit a pull request.

See `src/multilang_python/languages/template.json` and [USER_GUIDE.md](USER_GUIDE.md).

### 4. Code Contributions

To contribute code:
1. Fork and clone the repository:
   ```bash
   git clone https://github.com/<your-username>/multilang-python.git
   cd multilang-python
   ```
2. Create a branch:
   ```bash
   git checkout -b feature/<your-feature>
   ```
3. Set up development:
   ```bash
   pip install -r requirements/dev.txt
   python3 scripts/setup_dev.py
   ```
4. Write code:
   - Follow [ARCHITECTURE.md](ARCHITECTURE.md).
   - Use PEP 8 (enforced by `flake8`, see `config/flake8.ini`).
   - Add tests in `tests/`.
5. Test:
   ```bash
   python3 -m pytest tests/
   ```
6. Format:
   ```bash
   ./tools/format.sh
   ```
7. Commit and push:
   ```bash
   git commit -m "Add <feature>"
   ```
8. Submit a pull request using the [PR template](.github/PULL_REQUEST_TEMPLATE.md).

### 5. Improving Documentation

Update files in `docs/` (e.g., `USER_GUIDE.md`). Run:
```bash
python3 scripts/generate_docs.py
```
Submit a PR with changes.

### 6. Other Contributions

- Add benchmarks in `tests/benchmarks/`.
- Develop plugins in `src/multilang_python/interfaces/plugins/`.
- Translate documentation.
- Engage in GitHub Discussions.

## Development Workflow

- **Branch Naming**: `feature/<name>`, `bugfix/<name>`, `docs/<name>`.
- **Testing**: Use `pytest` (see `config/pytest.ini`).
- **Linting**: Run `./tools/lint.sh`.
- **CI/CD**: Ensure GitHub Actions pass.
- **Code Review**: PRs need one maintainer approval.

## Project Structure

See [ARCHITECTURE.md](ARCHITECTURE.md) for details. Key directories:
- `src/multilang_python/core/`: Transpileur and validator.
- `src/multilang_python/languages/`: JSON translations.
- `src/multilang_python/interfaces/`: CLI and plugins.
- `tests/`: Tests.
- `examples/`: Sample scripts.
- `docs/`: Documentation.

## Getting Help

- Search GitHub issues.
- Use GitHub Discussions.
- Contact maintainers via GitHub.

## License

Contributions are under the [MIT License](LICENSE).

Thank you for making **multilang-python** inclusive and powerful!
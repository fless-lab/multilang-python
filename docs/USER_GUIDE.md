# Multilang-Python User Guide

This guide explains how to use **multilang-python**, a transpileur that lets you write Python code in your native language (e.g., French `définir` instead of `def`) and translates it to standard Python.

## Installation

### Prerequisites
- Python 3.6+ ([python.org](https://www.python.org)).
- pip (included with Python).

### Install
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

### Update
```bash
pip install --upgrade multilang-python
```

## Writing Code

1. Create a `.py` file.
2. Add a language header, e.g.:
   ```python
   # multilang-python: fr
   ```
   Use language codes (e.g., `fr` for French). Check available languages:
   ```bash
   multilang-python --list-langs
   ```
3. Write code using native keywords. Example (`hello_world.py`):
   ```python
   # multilang-python: fr
   définir saluer(nom):
       afficher("Bonjour, " + nom)

   saluer("Monde")
   ```

See `examples/` for scripts (e.g., `examples/french/calculator.py`).

## Running Code

Run:
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

Save translated code:
```bash
multilang-python hello_world.py --output translated.py
```

Override header language:
```bash
multilang-python hello_world.py --lang es
```

## IDE Integration

### VSCode
Create `.vscode/tasks.json`:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Multilang-Python",
      "type": "shell",
      "command": "multilang-python ${file}",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```
Run with `Ctrl+Shift+B`.

### Other IDEs
Configure to run `multilang-python <file>`.

## Troubleshooting

- **“No language specified”**: Add `# multilang-python: <lang>` or use `--lang`.
- **“Language file not found”**: Check `--list-langs`. Add languages via [CONTRIBUTING.md](CONTRIBUTING.md).
- **Execution errors**: Review translated code.

## Further Reading

- [ARCHITECTURE.md](ARCHITECTURE.md): Project structure.
- [CONTRIBUTING.md](CONTRIBUTING.md): Contributing.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md): Community standards.
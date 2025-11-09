"""
Entry point for running multilang-python as a module.

Usage:
    python -m multilang_python [args]
"""

import sys
from .interfaces.cli import main

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Setup development environment for multilang-python.
"""

import os
import subprocess
import sys

def run_command(cmd, description, check=True):
    """Run a shell command and print status."""
    print(f"\n{'='*70}")
    print(f"  {description}")
    print(f"{'='*70}")
    print(f"Running: {cmd}\n")

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=check,
            capture_output=True,
            text=True
        )

        if result.stdout:
            print(result.stdout)

        if result.returncode == 0:
            print(f" {description} completed successfully")
        else:
            print(f"   {description} completed with warnings")
            if result.stderr:
                print(f"Stderr: {result.stderr}")

        return result.returncode == 0

    except subprocess.CalledProcessError as e:
        print(f"L {description} failed")
        print(f"Error: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is adequate."""
    print("=" * 70)
    print("  Checking Python version")
    print("=" * 70)

    version_info = sys.version_info
    print(f"Python {version_info.major}.{version_info.minor}.{version_info.micro}")

    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 7):
        print("L Python 3.7+ is required")
        return False

    print(" Python version is adequate")
    return True

def main():
    """Main entry point."""
    print("\n" + "=" * 70)
    print("  multilang-python: Development Environment Setup")
    print("=" * 70)

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

    if not in_venv:
        print("\n   WARNING: Not running in a virtual environment")
        print("It's recommended to use a virtual environment:")
        print("  python -m venv venv")
        print("  source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
        print()

        response = input("Continue anyway? (y/N): ").strip().lower()
        if response != 'y':
            print("Setup cancelled.")
            sys.exit(0)

    # Install package in development mode
    success = run_command(
        "pip install -e .",
        "Installing package in development mode"
    )

    if not success:
        print("\nL Failed to install package")
        sys.exit(1)

    # Check if dev requirements file exists
    dev_req_file = os.path.join(os.path.dirname(__file__), '..', 'dev-requirements.txt')

    if os.path.exists(dev_req_file):
        success = run_command(
            f"pip install -r {dev_req_file}",
            "Installing development dependencies"
        )

        if not success:
            print("\n   Failed to install some development dependencies")
    else:
        print("\n   No dev-requirements.txt found, installing common dev tools")

        # Install common development tools
        dev_tools = [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "isort>=5.12.0"
        ]

        for tool in dev_tools:
            run_command(
                f"pip install {tool}",
                f"Installing {tool.split('>=')[0]}",
                check=False
            )

    # Run validation
    print("\n" + "=" * 70)
    print("  Validating language files")
    print("=" * 70)

    validate_script = os.path.join(os.path.dirname(__file__), 'validate_all.py')

    if os.path.exists(validate_script):
        subprocess.run([sys.executable, validate_script])

    # Print success message
    print("\n" + "=" * 70)
    print("  Setup Complete!")
    print("=" * 70)
    print("\n Development environment is ready!")
    print("\nYou can now:")
    print("  " Run tests: pytest")
    print("  " Format code: black .")
    print("  " Check linting: flake8")
    print("  " Run the CLI: multilang-python --help")
    print("  " Validate languages: python scripts/validate_all.py")
    print()

if __name__ == "__main__":
    main()

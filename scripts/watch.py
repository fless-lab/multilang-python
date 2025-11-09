#!/usr/bin/env python3
"""
Watch mode for multilang-python: automatically translate files when they change.
"""

import argparse
import os
import sys
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from src.core.transpiler import Transpiler
    from src.core.utils import read_file, write_file
except ImportError:
    print("L Error: Could not import multilang-python modules")
    print("Make sure you run this from the project root directory")
    sys.exit(1)

class FileWatcher:
    """Watch files for changes and auto-translate them."""

    def __init__(self, paths, lang_code=None, output_dir=None, interval=1.0):
        """
        Initialize the file watcher.

        Args:
            paths: List of file/directory paths to watch
            lang_code: Language code to use (if None, detect from file header)
            output_dir: Directory to write translated files (if None, use same dir as source)
            interval: How often to check for changes (seconds)
        """
        self.paths = paths
        self.lang_code = lang_code
        self.output_dir = output_dir
        self.interval = interval
        self.file_mtimes = {}

    def get_files_to_watch(self):
        """Get list of all Python files to watch."""
        files = []

        for path in self.paths:
            path = Path(path)

            if path.is_file():
                if path.suffix == '.py':
                    files.append(path)
            elif path.is_dir():
                files.extend(path.rglob('*.py'))

        return files

    def get_output_path(self, source_path):
        """Get the output path for a translated file."""
        source_path = Path(source_path)

        if self.output_dir:
            # Use output directory, preserving filename
            output_dir = Path(self.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            return output_dir / source_path.name
        else:
            # Same directory, add _translated suffix
            return source_path.parent / f"{source_path.stem}_translated{source_path.suffix}"

    def translate_file(self, file_path):
        """Translate a single file."""
        try:
            # Read the file
            code = read_file(str(file_path))

            # Detect language from header or use specified language
            lang_code = self.lang_code
            if not lang_code:
                detected_lang = Transpiler.get_language_from_header(code)
                if detected_lang:
                    lang_code = detected_lang
                else:
                    print(f"   {file_path.name}: No language header found and no --lang specified, skipping")
                    return False

            # Translate
            transpiler = Transpiler(lang_code=lang_code)
            translated = transpiler.translate(code)

            # Write output
            output_path = self.get_output_path(file_path)
            write_file(str(output_path), translated)

            print(f" {file_path.name} -> {output_path.name}")
            return True

        except Exception as e:
            print(f"L Error translating {file_path.name}: {e}")
            return False

    def check_for_changes(self):
        """Check all watched files for modifications."""
        files = self.get_files_to_watch()
        changed_files = []

        for file_path in files:
            try:
                current_mtime = file_path.stat().st_mtime

                if str(file_path) not in self.file_mtimes:
                    # New file
                    self.file_mtimes[str(file_path)] = current_mtime
                    changed_files.append(file_path)
                elif self.file_mtimes[str(file_path)] != current_mtime:
                    # Modified file
                    self.file_mtimes[str(file_path)] = current_mtime
                    changed_files.append(file_path)

            except Exception as e:
                print(f"   Error checking {file_path}: {e}")

        return changed_files

    def watch(self):
        """Start watching files."""
        print("=" * 70)
        print("  multilang-python: Watch Mode")
        print("=" * 70)

        files = self.get_files_to_watch()

        if not files:
            print("\nL No Python files found to watch")
            return

        print(f"\n=@ Watching {len(files)} file(s)...")
        print(f"Language: {self.lang_code or 'auto-detect'}")
        print(f"Output: {self.output_dir or 'same directory (_translated.py)'}")
        print("\nPress Ctrl+C to stop\n")

        # Initial translation
        print("Performing initial translation...")
        for file_path in files:
            self.translate_file(file_path)

        # Watch for changes
        try:
            while True:
                time.sleep(self.interval)

                changed_files = self.check_for_changes()

                if changed_files:
                    print(f"\n=Ý Detected {len(changed_files)} change(s)...")
                    for file_path in changed_files:
                        self.translate_file(file_path)

        except KeyboardInterrupt:
            print("\n\n=K Watch mode stopped")

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Watch Python files and auto-translate them with multilang-python"
    )

    parser.add_argument(
        'paths',
        nargs='+',
        help='Files or directories to watch'
    )

    parser.add_argument(
        '--lang',
        '-l',
        help='Language code (if not specified, will detect from file header)'
    )

    parser.add_argument(
        '--output',
        '-o',
        help='Output directory for translated files'
    )

    parser.add_argument(
        '--interval',
        '-i',
        type=float,
        default=1.0,
        help='Check interval in seconds (default: 1.0)'
    )

    args = parser.parse_args()

    # Create watcher and start
    watcher = FileWatcher(
        paths=args.paths,
        lang_code=args.lang,
        output_dir=args.output,
        interval=args.interval
    )

    watcher.watch()

if __name__ == "__main__":
    main()

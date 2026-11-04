import sys
import os

from multilang_python.core.transpiler import Transpiler
from multilang_python.core.utils import read_file, write_file
from multilang_python.core.utils import setup_logging


def main():
    """Main CLI for multilang-python."""
    logger = setup_logging()

    usage = (
        "Usage: multilang-python <input_file> "
        "[--output <output_file>] [--lang <lang>]\n"
        "       multilang-python --list-langs\n"
        "       multilang-python --version\n"
        "       multilang-python --help"
    )

    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)

    if sys.argv[1] in ("--help", "-h"):
        print(usage)
        sys.exit(0)

    if sys.argv[1] == "--version":
        print("multilang-python 0.1.0")
        sys.exit(0)

    if sys.argv[1] == "--list-langs":
        lang_dir = os.path.join(
            os.path.dirname(__file__), "..", "languages"
        )

        langs = sorted(
            f.removesuffix(".json")
            for f in os.listdir(lang_dir)
            if f.endswith(".json")
            and f not in ("template.json", "schema.json")
        )

        print("Available languages:", langs)
        sys.exit(0)

    input_file = sys.argv[1]
    output_file = None
    lang_code = None

    # Parse arguments
    i = 2

    while i < len(sys.argv):

        if sys.argv[i] == "--output" and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
            i += 2

        elif sys.argv[i] == "--lang" and i + 1 < len(sys.argv):
            lang_code = sys.argv[i + 1]
            i += 2

        else:
            print("Invalid argument:", sys.argv[i])
            sys.exit(1)

    if not os.path.isfile(input_file):
        print("Error: Input file not found.")
        sys.exit(1)

    code = read_file(input_file)

    if not lang_code:
        lang_code = Transpiler.get_language_from_header(code)

        if not lang_code:
            print(
                "Error: No language specified. "
                "Use '# multilang-python: <lang>' "
                "header or --lang <lang>."
            )
            sys.exit(1)

    # Initialize transpiler
    try:
        trans = Transpiler(lang_code=lang_code)

    except Exception as e:
        logger.error(f"Initialization error: {e}")
        print(f"Error: {e}")
        sys.exit(1)

    # Translate source code
    try:
        translated_code = trans.translate(code)

        print("Translated code:")
        print(translated_code)

    except Exception as e:
        logger.error(f"Translation error: {e}")
        print(f"Error: {e}")
        sys.exit(1)

    # Save translated code if requested
    if output_file:
        try:
            write_file(output_file, translated_code)
            logger.info(
                f"Translated code saved to {output_file}"
            )

        except Exception as e:
            logger.error(f"File writing error: {e}")
            print(f"Error writing output file: {e}")
            sys.exit(1)

    # Execute translated Python code
    try:
        namespace = {
            "__name__": "__main__",
            "__builtins__": __builtins__,
            "__file__": os.path.abspath(input_file),
            "__package__": None,
        }

        exec(
            compile(
                translated_code,
                os.path.abspath(input_file),
                "exec"
            ),
            namespace,
            namespace
        )

    except Exception as e:
        logger.error(f"Execution error: {e}")
        print(f"Execution error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
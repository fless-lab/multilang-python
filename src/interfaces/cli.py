import sys
import os
from multilang_python.core.transpiler import Transpiler
from multilang_python.core.utils import read_file, write_file, setup_logging

def main():
    """Main CLI for multilang-python."""
    logger = setup_logging()

    if len(sys.argv) < 2:
        print("Usage: multilang-python <input_file> [--output <output_file>] [--lang <lang>] [--list-langs] [--version]")
        sys.exit(1)

    if sys.argv[1] == '--version':
        print("multilang-python 0.1.0")
        sys.exit(0)

    if sys.argv[1] == '--list-langs':
        lang_dir = os.path.join(os.path.dirname(__file__), '..', 'languages')
        langs = [f.split('.')[0] for f in os.listdir(lang_dir) if f.endswith('.json') and f != 'template.json' and f != 'schema.json']
        print("Available languages:", langs)
        sys.exit(0)

    input_file = sys.argv[1]
    output_file = None
    lang_code = None

    # Parse arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--output' and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--lang' and i + 1 < len(sys.argv):
            lang_code = sys.argv[i + 1]
            i += 2
        else:
            print("Invalid argument:", sys.argv[i])
            sys.exit(1)

    if not os.path.exists(input_file):
        print("Error: Input file not found.")
        sys.exit(1)

    code = read_file(input_file)

    if not lang_code:
        lang_code = Transpiler.get_language_from_header(code)
        if not lang_code:
            print("Error: No language specified. Use '# multilang-python: <lang>' header or --lang <lang>.")
            sys.exit(1)

    try:
        trans = Transpiler(lang_code=lang_code)
    except Exception as e:
        logger.error(f"Initialization error: {e}")
        print(f"Error: {e}")
        sys.exit(1)

    try:
        translated_code = trans.translate(code)
        print("Translated code:")
        print(translated_code)
    except Exception as e:
        logger.error(f"Translation error: {e}")
        print(f"Error: {e}")
        sys.exit(1)

    if output_file:
        write_file(output_file, translated_code)
        logger.info(f"Translated code saved to {output_file}")

    try:
        exec(translated_code)
    except Exception as e:
        logger.error(f"Execution error: {e}")
        print(f"Execution error: {e}")

if __name__ == '__main__':
    main()
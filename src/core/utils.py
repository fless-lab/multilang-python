import logging
import os

def setup_logging():
    """Set up basic logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('multilang-python.log')
        ]
    )
    return logging.getLogger('multilang_python')

def read_file(file_path, as_json=False):
    """Read a file with UTF-8 encoding.

    Args:
        file_path: Path to the file to read
        as_json: If True, parse and return JSON content

    Returns:
        File content as string or parsed JSON dict/list
    """
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        if as_json:
            return json.loads(content)
        return content

def write_file(file_path, content):
    """Write content to a file with UTF-8 encoding."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
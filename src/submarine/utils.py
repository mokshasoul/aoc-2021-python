from pathlib import Path


def open_input_file(file_path):
    parent_path = Path(file_path).parent
    return (parent_path / 'input.txt').read_text().splitlines()
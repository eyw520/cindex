import fnmatch
import os
from pathlib import Path

import yaml


def load_config(config_path: str):
    """
    Load the configuration from the YAML settings file.
    """
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def matches_scope(filepath, scope, root):
    """
    Check if a file matches the scope.
    """
    relative_path = os.path.relpath(filepath, root)
    relative_path_posix = Path(relative_path).as_posix()
    path_parts = Path(relative_path_posix).parts

    exclude_patterns = scope.get("exclude", [])
    for pattern in exclude_patterns:
        if pattern.endswith("/"):
            folder_name = pattern.rstrip("/")
            if folder_name in path_parts:
                return False
        elif fnmatch.fnmatch(relative_path_posix, pattern):
            return False

    include_patterns = scope.get("include", [])
    for pattern in include_patterns:
        if fnmatch.fnmatch(relative_path_posix, pattern):
            return True

    return False


def walk_and_filter_files(root, scope):
    """
    Walk the directory and filter files based on the scope.
    """
    matched_files = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if matches_scope(full_path, scope, root):
                matched_files.append(full_path)
    return matched_files


def read_file_contents(file_path, root):
    """
    Read and format contents of a single file.
    """
    rel_path = os.path.relpath(file_path, root)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            contents = f.read()
        return f"\n== File: {rel_path} ==\n{contents}\n"
    except Exception as e:
        return f"\n== File: {rel_path} ==\nError reading {rel_path}: {e}\n"


def write_output(matched_files, output_path, root):
    """
    Write contents of all matched files to output file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as output_file:
        for file_path in matched_files:
            file_contents = read_file_contents(file_path, root)
            output_file.write(file_contents)

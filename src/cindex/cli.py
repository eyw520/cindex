#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from cindex.utils.read import (
    load_config,
    read_file_contents,
    walk_and_filter_files,
)


def get_default_settings_path():
    return Path(__file__).parent / "configs" / "default-settings.yml"


def main():
    parser = argparse.ArgumentParser(description="Index a codebase as context for LLMs.")
    parser.add_argument(
        "--config",
        nargs="?",
        default=None,
        help="Optional path to config file (defaults to default-settings.yml)",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--list",
        action="store_true",
        help="List matched file names instead of printing file contents.",
    )
    group.add_argument(
        "--count",
        action="store_true",
        help="Print the total word count of all matched file contents.",
    )
    args = parser.parse_args()

    root = Path(".").resolve()
    config_path = args.config if args.config else get_default_settings_path()

    if not root.exists() or not root.is_dir():
        print(f"Error: Directory '{root}' does not exist or is not a directory.", file=sys.stderr)
        sys.exit(1)

    config = load_config(config_path)
    scope = config.get("scope", {})

    matched_files = walk_and_filter_files(root, scope)
    if args.list:
        for file_path in matched_files:
            print(Path(file_path).relative_to(root))
    elif args.count:
        total_words = 0
        for file_path in matched_files:
            contents = read_file_contents(file_path, root)
            total_words += len(contents.split())
        print(total_words)
    else:
        for file_path in matched_files:
            print(read_file_contents(file_path, root))


if __name__ == "__main__":
    main()

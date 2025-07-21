# CodeContext

## Overview

This project will serve as the backend and infrastructure for `codecontext`, a lightweight script that helps you index a codebase as context for LLMs.

## Setup

This project uses `poetry` to manage dependencies. To install the project, run the following commands:

```bash
python -m venv .venv
source .venv/bin/activate
poetry install
```

## Usage

This project can be installed in editable mode using the following command:

```bash
pip install -e .
```

This creates a CLI command `cindex` that can be used to index a codebase.

```bash
cindex <optional_target_directory> [optional_config_path]
```

The `config_path` is optional and defaults to `src/cindex/configs/default-settings.yml`.

This command can be added to your shell's `PATH` to make it available globally.

```bash
export PATH="$PATH:/path/to/code-context/.venv/bin"
```
SHELL := /bin/zsh

code-cleanup:
	source .venv/bin/activate && \
		poetry run isort . && \
		poetry run black .

install:
	poetry install --no-root

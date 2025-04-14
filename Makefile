.PHONY: format test

default: test

format:
	uv run ruff format .

test:
	uv run pytest -v

serve:
	uv run fastapi dev main.py

all: format test

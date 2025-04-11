.PHONY: format test

default: test

format:
	uv run ruff format .

test:
	uv run pytest

all: format test

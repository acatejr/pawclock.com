.PHONY: format test

default: test

format:
	uv run ruff format .

test:
	uv run pytest -vs

serve:
	uv run fastapi dev main.py

test-models:
	uv run pytest -vs tests/test_models.py

all: format test

.PHONY: format test

default: test

format:
	uv run ruff format .

test:
	uv run pytest -vs

serve:
	uv run manage.py runserver

test-models:
	uv run pytest -vs tests/test_models.py

migrate:
	uv run manage.py migrate

all: format test

install:
	uv sync

run:
	uv run uvicorn apps.main:app --reload
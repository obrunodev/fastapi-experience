install:
	uv sync

run:
	uv run uvicorn apps.main:app --reload

migration:
	uv run alembic revision --autogenerate -m "$(msg)"

upgrade:
	uv run alembic upgrade head

downgrade:
	uv run alembic downgrade -1

history:
	uv run alembic history

current:
	uv run alembic current
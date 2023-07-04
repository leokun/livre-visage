dev:
	poetry run uvicorn backend.main:app --reload

lint:
	poetry run pycln backend --check
	poetry run isort backend --check
	poetry run black backend --check
	poetry run pylint backend

lint-fix:
	poetry run pycln backend
	poetry run isort backend
	poetry run black backend

test: poetry run pytest
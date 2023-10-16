# Backend

## Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Psycopg2](https://www.psycopg.org/docs/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Poetry](https://python-poetry.org/)
- [Pytest](https://docs.pytest.org/en/7.4.x/)
- [Ruff](https://docs.astral.sh/ruff/)
- [Black](https://black.readthedocs.io/en/stable/)
- [Mypy](https://mypy-lang.org/)

## Run

Install [Poetry](https://python-poetry.org/docs/)  
Set config for venv in local

```bash
poetry config virtualenvs.in-project true
```

Set database URL in .env file

```bash
poetry install
poetry shell
alembic upgrade head
uvicorn src.main:app --reload
```

## Troubleshoot

- On Mac, if you have issue installing psycopg2 library, install postgresql:

```bash
brew install postgresql
```

## Api docs

- [Swagger](http://localhost:8000/docs)
- [Redoc](http://localhost:8000/redoc)

## Tests

```bash
poetry run pytest --cov=src --cov-report=term
```

## Lint

```bash
# ruff, mypy
poetry run scripts/lint.sh
```

## Format

```bash
# ruff, black
poetry run scripts/format.sh
```

## New revision

```bash
poetry run alembic revision --autogenerate -m "<name>"
```

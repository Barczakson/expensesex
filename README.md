# expensesex

FastAPI app using asyncpg with a src/ layout.

## Setup

1) Create and activate a Python 3.10 virtualenv

```
python3.10 -m venv expensesexc
source expensesexc/bin/activate
```

2) Install dependencies

```
pip install -r requirements.txt -r requirements-dev.txt
```

3) Configure environment

Set `DATABASE_URL` in a `.env` at the repo root, e.g.:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/expenses
```

## Run

Use the module entrypoint (src layout requires `PYTHONPATH=src` unless installed):

```
PYTHONPATH=src python -m expensesex
```

Or run Uvicorn directly:

```
PYTHONPATH=src uvicorn expensesex.main:app --reload
```

Health endpoints:
- `GET /health/app`
- `GET /health/db`

## Tests

Run pytest (add tests under `tests/`):

```
pytest -q
```

With coverage:

```
pytest --maxfail=1 --disable-warnings -q --cov=expensesex
```

## Lint, Format, Types

```
ruff check .
ruff format .  # or: black . && isort .
mypy .
```

## Notes

- Source code lives under `src/expensesex/`.
- Pre-commit is configured for ruff, isort, black, and mypy.
- CI uses PostgreSQL and runs tests with coverage for `expensesex`.

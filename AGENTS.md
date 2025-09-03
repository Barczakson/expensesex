# Repository Guidelines

## Project Structure & Module Organization

- Current layout: `README.md` and a local Python virtual environment in `expensesexc/` (Python 3.10). Source code and tests are not yet added.
- Preferred layout:
  - `src/expensesex/`: application/package modules.
  - `tests/`: test modules mirroring `src/` (e.g., `tests/test_api.py`).
  - `assets/` (optional): static fixtures or sample data.
  - `requirements.txt` and `requirements-dev.txt`: runtime and dev deps.
  - Do not commit virtualenvs; use `.gitignore` to exclude `expensesexc/`.

## Build, Test, and Development Commands

- Setup env: `python3.10 -m venv expensesexc && source expensesexc/bin/activate`.
- Install deps: `pip install -r requirements.txt -r requirements-dev.txt`.
- Run tests: `pytest -q`.
- Lint/format: `ruff check . && ruff format .` (or `black . && isort .`).
- Run module: `python -m expensesex` (adjust to your entrypoint in `src/`).

## Coding Style & Naming Conventions

- Follow PEP 8; prefer explicit, typed code (use `mypy` for type checks).
- Indentation: 4 spaces; max line length 88.
- Naming: packages `lower_snake`, classes `PascalCase`, functions/vars `snake_case`.
- Keep modules focused; avoid large files. Public APIs live under `src/expensesex/`.

## Testing Guidelines

- Framework: `pytest` with `pytest-cov` for coverage.
- Name tests `test_*.py`; mirror module paths (e.g., `src/expensesex/foo.py` → `tests/test_foo.py`).
- Aim for meaningful unit tests; add integration tests for IO boundaries.
- Run locally: `pytest --maxfail=1 --disable-warnings -q --cov=expensesex`.

## Commit & Pull Request Guidelines

- Commits: concise imperative subject (≤72 chars). Example: `feat(parser): support CSV import`.
- Group related changes; avoid formatting-only noise mixed with logic changes.
- PRs: clear description, rationale, and scope; link related issues; include before/after notes or screenshots if behavior changes.
- CI should pass (tests, lint, type checks). Add/adjust tests for new behavior.

## Security & Configuration Tips

- Never commit secrets; use environment variables and `.env.sample` for documentation.
- Exclude virtualenvs and caches: add `.gitignore` entries for `expensesexc/`, `.venv/`, `.pytest_cache/`, `__pycache__/`.
- Pin dependencies where possible and update regularly.

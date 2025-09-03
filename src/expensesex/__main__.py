"""Run the app via `python -m expensesex`.

Uses Uvicorn with reload for local development.
"""

from __future__ import annotations

import os


def main() -> None:
    # Delay import so env is loaded before server boot
    import uvicorn

    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    # Use import string path to enable reload
    uvicorn.run("expensesex.main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    main()

from typing import AsyncIterator, Optional

import asyncpg

from expensesex.core.settings import settings

POOL: Optional[asyncpg.Pool] = None


async def init_pool() -> None:
    """Tworzy pulę połączeń raz, na starcie aplikacji."""
    global POOL
    if POOL is None:
        if not settings.DATABASE_URL:
            raise RuntimeError("DATABASE_URL is not set")
        POOL = await asyncpg.create_pool(
            dsn=settings.DATABASE_URL,
            statement_cache_size=0,
            max_inactive_connection_lifetime=30.0,
            min_size=1,
            max_size=5,  # dostosuj pod obciążenie
        )


async def close_pool() -> None:
    """Czyści pulę na zamknięcie aplikacji."""
    global POOL
    if POOL is not None:
        await POOL.close()
        POOL = None


async def get_conn() -> AsyncIterator[asyncpg.Connection]:
    """Dependency do FastAPI: daje połączenie na czas requestu."""
    assert POOL is not None, "DB pool not initialized"
    conn = await POOL.acquire()
    try:
        yield conn
    finally:
        await POOL.release(conn)

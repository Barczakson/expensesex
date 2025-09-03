from collections.abc import Generator

import pytest
from httpx import ASGITransport, AsyncClient

from expensesex.db import pool as db_pool
from expensesex.main import app


@pytest.fixture(autouse=True)
def patch_db_pool(monkeypatch: pytest.MonkeyPatch) -> Generator[None, None, None]:
    """Make init/shutdown no-ops so tests don't require a real DB."""

    async def _noop(*_args, **_kwargs):  # type: ignore[no-untyped-def]
        return None

    monkeypatch.setattr(db_pool, "init_pool", _noop)
    monkeypatch.setattr(db_pool, "close_pool", _noop)
    yield


@pytest.fixture()
def override_db_dependency() -> Generator[None, None, None]:
    """Override the get_conn dependency with a fake connection provider."""

    async def _fake_conn():  # type: ignore[no-untyped-def]
        class FakeConn:  # minimal stub; extend if endpoints start using it
            pass

        yield FakeConn()

    app.dependency_overrides[db_pool.get_conn] = _fake_conn
    try:
        yield
    finally:
        app.dependency_overrides.pop(db_pool.get_conn, None)


@pytest.mark.asyncio
async def test_health_app() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/health/app")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_health_db(override_db_dependency: None) -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/health/db")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}

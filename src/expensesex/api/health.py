from typing import Dict

import asyncpg
from fastapi import APIRouter, Depends

from expensesex.db.pool import get_conn

router = APIRouter()


@router.get("/health/app")
async def health_app() -> Dict[str, str]:
    return {"status": "ok"}


@router.get("/health/db")
async def health_db(conn: asyncpg.Connection = Depends(get_conn)) -> Dict[str, str]:
    return {"status": "ok"}

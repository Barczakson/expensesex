from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from expensesex.api.health import router as health_router
from expensesex.db.pool import close_pool, init_pool

# @app.on_event("startup")
# async def startup() -> None:
#   await init_pool()


# @app.on_event("shutdown")
# async def shutdown() -> None:
#   await close_pool()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await init_pool()
    yield
    await close_pool()


app = FastAPI(lifespan=lifespan)

app.include_router(health_router)

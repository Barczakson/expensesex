"""Application settings loaded from environment and .env files.

We support two local locations for convenience:
- project root: .env
- app/.env (legacy) — loaded if present
"""

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolve repository root from this file location after src-layout move:
# src/expensesex/core/settings.py -> repo root is parents[3]
ROOT_DIR = Path(__file__).resolve().parents[3]

# Load env files (do not override already exported vars)
load_dotenv(ROOT_DIR / ".env", override=False)
load_dotenv(ROOT_DIR / "app/.env", override=False)


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    model_config = SettingsConfigDict(
        env_file=str(ROOT_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

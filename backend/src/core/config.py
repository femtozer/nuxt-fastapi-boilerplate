import logging
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    ENV: str = "local"
    LOG_LEVEL: int = logging.INFO
    PROJECT_NAME: str = "Todos App"
    API_PREFIX: str = "/api"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]  # default origins: nuxt
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:postgres@localhost:5432/todos"
    MAX_PAGE_SIZE: int = 100


settings = Settings()

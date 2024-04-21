from typing import List, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str
    port: int
    origins: None | list[str]

    echo: bool
    postgres_user: str
    postgres_password: str
    postgres_db: str

    redis_host: str
    redis_port: int

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()

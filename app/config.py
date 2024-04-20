from typing import List, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str
    port: int
    origins: Optional[List[str]]

    database_url: str
    echo: bool

    redis_host: str
    redis_port: int

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()

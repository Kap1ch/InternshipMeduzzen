from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str
    port: int
    origins: list[str]


    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
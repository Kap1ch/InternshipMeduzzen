import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict

root_dir = pathlib.Path(__file__).parent.parent
FILE_DATA = root_dir.joinpath('.env')


class Settings(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(env_file=FILE_DATA)


settings = Settings()
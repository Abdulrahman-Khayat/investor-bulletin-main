from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    rapid_api_url: str
    x_rapid_api_key: str
    x_rapid_api_host: str
    database_url: str

    model_config = SettingsConfigDict(env_file="../../.env")

settings = Settings()

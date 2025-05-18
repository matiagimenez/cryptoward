from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    DATASOURCE_URL: str
    DATASOURCE_NAME: str
    DATASOURCE_DESCRIPTION: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


Settings = ApplicationSettings()

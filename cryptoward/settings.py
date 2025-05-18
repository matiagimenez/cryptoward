from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    DATASOURCE_URL: str = "https://coinmarketcap.com/currencies"

    KAFKA_HOST: str
    KAFKA_TOPIC: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


Settings = ApplicationSettings()

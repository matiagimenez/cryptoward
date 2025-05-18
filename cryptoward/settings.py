from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    DATASOURCE_URL: str = "https://coinmarketcap.com/currencies"

    KAFKA_HOST: str
    KAFKA_TOPIC: str


Settings = ApplicationSettings()

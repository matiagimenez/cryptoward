from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    DATASOURCE_URL: str = "https://coinmarketcap.com/currencies"

    KAFKA_HOST: str = "localhost:29092"
    KAFKA_TOPIC: str = "cryptoward-events"

    SCHEDULE_TIME_IN_MINUTES: int = 1


Settings = ApplicationSettings()

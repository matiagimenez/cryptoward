from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    DATASOURCE_URL: str = "https://coinmarketcap.com/currencies"
    SCHEDULE_TIME_IN_MINUTES: int = 1

    @property
    def CRYPTOCURRENCIES(self) -> list[str]:
        return ["bitcoin", "ethereum", "dogecoin"]


Settings = ApplicationSettings()

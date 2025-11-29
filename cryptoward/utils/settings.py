from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATASOURCE_URL: str
    TELEGRAM_BOT_TOKEN: str

    @property
    def CRYPTOCURRENCIES(self) -> list[str]:
        return ["bitcoin", "ethereum", "solana", "bnb", "aave", "avalanche", "monero"]


Settings = ApplicationSettings()  # type: ignore[call-arg]]

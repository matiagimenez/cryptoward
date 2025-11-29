from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATASOURCE_URL: str = "https://coinmarketcap.com/currencies"
    TELEGRAM_BOT_TOKEN: str = ""
    PRICE_ELEMENT_TAG: str = "span"
    PRICE_ELEMENT_ATTRIBUTES: dict[str, str] = {"data-test": "text-cdp-price-display"}

    @property
    def CRYPTOCURRENCIES(self) -> list[str]:
        return ["bitcoin", "ethereum", "solana", "bnb", "aave", "avalanche", "monero"]


Settings = ApplicationSettings()

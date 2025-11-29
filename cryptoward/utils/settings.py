from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATASOURCE_URL: str
    TELEGRAM_BOT_TOKEN: str
    PRICE_ELEMENT_TAG: str = "span"
    PRICE_ELEMENT_ATTRS: dict[str, str] = {"data-test": "text-cdp-price-display"}

    @property
    def CRYPTOCURRENCIES(self) -> list[str]:
        return ["bitcoin", "ethereum", "solana", "bnb", "aave", "avalanche", "monero"]

    @property
    def BOT_COMMANDS(self) -> list[tuple[str, str]]:
        return [
            ("start", "Start the bot and see welcome message"),
            ("set", "Set daily alert (e.g., /set 09.30)"),
            ("help", "Get usage instructions"),
            ("remove", "Remove daily alert"),
        ]


Settings = ApplicationSettings()  # type: ignore[call-arg]

from cryptoward.bot import TelegramBot, build_telegram_application
from cryptoward.models import Element
from cryptoward.services import CryptoService


def main() -> None:
    application = build_telegram_application()
    element = Element(
        tag="span",
        data_attributes={"data-test": "text-cdp-price-display"},
    )
    crypto_service = CryptoService(element=element)
    bot = TelegramBot(application=application, crypto_service=crypto_service)
    bot.run()


if __name__ == "__main__":
    main()

from cryptoward.bot import TelegramBot, build_bot_application
from cryptoward.services import CryptoService


def main() -> None:
    application = build_bot_application()
    crypto_service = CryptoService.from_settings()
    bot = TelegramBot(application=application, crypto_service=crypto_service)
    bot.run()


if __name__ == "__main__":
    main()

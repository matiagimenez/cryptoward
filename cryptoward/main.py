from telegram.ext import ApplicationBuilder, PicklePersistence

from cryptoward.bot import TelegramBot
from cryptoward.models import Element
from cryptoward.services import CryptoService
from cryptoward.utils import Settings


def main() -> None:
    application = (
        ApplicationBuilder()
        .token(Settings.TELEGRAM_BOT_TOKEN)
        .persistence(PicklePersistence(filepath="data/bot_storage.pickle"))
        .build()
    )
    element = Element(
        tag="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    crypto_service = CryptoService(element=element)
    bot = TelegramBot(application=application, crypto_service=crypto_service)
    bot.run()


if __name__ == "__main__":
    main()

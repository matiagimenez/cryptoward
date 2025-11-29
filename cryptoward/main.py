from telegram import BotCommand
from telegram.ext import Application, ApplicationBuilder, PicklePersistence

from cryptoward.bot import TelegramBot
from cryptoward.models import Element
from cryptoward.services import CryptoService
from cryptoward.utils import Settings


async def post_init(application: Application) -> None:
    """
    Set up the bot's command menu on startup.
    """
    commands = [
        BotCommand("start", "Start the bot and see welcome message"),
        BotCommand("set", "Set daily alert (e.g., /set 09.30)"),
        BotCommand("help", "Get usage instructions"),
        BotCommand("remove", "Remove daily alert"),
    ]
    await application.bot.set_my_commands(commands)


def main() -> None:
    application = (
        ApplicationBuilder()
        .token(Settings.TELEGRAM_BOT_TOKEN)
        .persistence(PicklePersistence(filepath="data/bot_storage.pickle"))
        .post_init(post_init)
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

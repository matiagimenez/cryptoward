from telegram import BotCommand
from telegram.ext import Application, ApplicationBuilder, PicklePersistence

from cryptoward.utils import Settings


async def post_init(application: Application) -> None:
    commands = [
        BotCommand("start", "Start the bot and see welcome message"),
        BotCommand("set", "Set daily alert (e.g., /set 09.30)"),
        BotCommand("help", "Get usage instructions"),
        BotCommand("remove", "Remove daily alert"),
        BotCommand("clear", "Clear conversation history"),
    ]
    await application.bot.set_my_commands(commands)


def build_application() -> Application:
    return (
        ApplicationBuilder()
        .token(Settings.TELEGRAM_BOT_TOKEN)
        .persistence(PicklePersistence(filepath="data/bot_storage.pickle"))
        .post_init(post_init)
        .build()
    )

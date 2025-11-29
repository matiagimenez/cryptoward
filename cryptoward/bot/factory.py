from telegram.ext import Application, ApplicationBuilder, PicklePersistence

from cryptoward.utils import Settings

from .config import BOT_COMMANDS_DESCRIPTIONS


async def post_init_configuration(application: Application) -> None:
    await application.bot.set_my_commands(BOT_COMMANDS_DESCRIPTIONS)


def build_bot_application() -> Application:
    return (
        ApplicationBuilder()
        .token(Settings.TELEGRAM_BOT_TOKEN)
        .persistence(PicklePersistence(filepath="data/bot_storage.pickle"))
        .post_init(post_init_configuration)
        .build()
    )

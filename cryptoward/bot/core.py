import datetime
from dataclasses import dataclass

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from cryptoward.services import CryptoService
from cryptoward.utils import Level, log

from .config import WELCOME_MESSAGE


@dataclass
class TelegramBot:
    crypto_service: CryptoService
    application: Application

    @property
    def commands(self) -> list[CommandHandler]:
        return [
            CommandHandler(["start", "help"], self.start),
            CommandHandler("set", self.set_job),
            CommandHandler("remove", self.unset_job),
        ]

    async def send_prices(self, context: ContextTypes.DEFAULT_TYPE) -> None:
        prices = self.crypto_service.fetch_cryptocurrency_prices()
        message = "\n".join(prices)
        await context.bot.send_message(chat_id=context.job.chat_id, text=message)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        log(
            f"User started the bot with chat_id: {update.effective_message.chat_id}",
            Level.INFO,
        )
        log(f"context: {context}", Level.INFO)
        await update.message.reply_text(WELCOME_MESSAGE)

    def unset_job(self, name: str, context: ContextTypes.DEFAULT_TYPE) -> None:
        current_jobs = context.job_queue.get_jobs_by_name(name)
        if current_jobs:
            for job in current_jobs:
                job.schedule_removal()

    async def set_job(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        chat_id = update.effective_message.chat_id
        log(f"Setting daily job for chat_id: {chat_id}", Level.INFO)
        try:
            time_input: str = context.args[0]
            hour, minute = map(int, time_input.split("."))
            time = datetime.time(
                hour=hour,
                minute=minute,
                tzinfo=datetime.UTC,
            )

            self.unset_job(str(chat_id), context)

            context.job_queue.run_daily(
                self.send_prices,
                time=time,
                chat_id=chat_id,
                name=str(chat_id),
                data=time_input,
            )
            await update.effective_message.reply_text(f"Timer set for {time} UTC.")
        except (IndexError, ValueError):
            await update.effective_message.reply_text(WELCOME_MESSAGE)

    def run(self) -> None:
        log("Starting Cryptoward Bot", Level.INFO)
        for command in self.commands:
            self.application.add_handler(command)
        self.application.run_polling()

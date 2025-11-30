"""
Serverless webhook handler for Telegram bot using FastAPI.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request, Response
from telegram import Update

from cryptoward.bot import TelegramBot, build_bot_application
from cryptoward.services import CryptoService
from cryptoward.utils import Level, log

bot_app = None
bot_instance = None


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Lifespan context manager to initialize and shutdown the bot application."""
    global bot_app, bot_instance

    log("Initializing bot application", Level.INFO)
    bot_app = build_bot_application()
    crypto_service = CryptoService.from_settings()
    bot_instance = TelegramBot(application=bot_app, crypto_service=crypto_service)

    # Register command handlers
    for command in bot_instance.commands:
        bot_app.add_handler(command)

    await bot_app.initialize()
    log("Bot application initialized", Level.INFO)

    yield

    # Cleanup on shutdown
    log("Shutting down bot application", Level.INFO)
    await bot_app.shutdown()


app = FastAPI(title="Cryptoward Webhook", lifespan=lifespan)

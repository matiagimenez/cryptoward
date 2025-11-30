"""
Serverless webhook handler for Telegram bot using FastAPI.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import APIRouter, Request
from telegram import Update

from cryptoward.bot import TelegramBot, build_bot_application
from cryptoward.services import CryptoService
from cryptoward.utils import Level, log

router = APIRouter()


@router.get("/")
@router.get("/api/webhook")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "Cryptoward bot webhook is running"}


@router.post("/api/webhook")
async def webhook(request: Request):
    """Handle incoming webhook POST requests from Telegram."""
    try:
        # Parse the update from Telegram
        update_data = await request.json()
        log(f"Received update: {update_data}", Level.INFO)

        # Process the update
        if bot_app:
            update = Update.de_json(update_data, bot_app.bot)
            await bot_app.process_update(update)

        return {"ok": True}

    except Exception as e:
        log(f"Error processing webhook: {str(e)}", Level.ERROR)
        return {"error": str(e)}

"""
Script to set up the Telegram webhook for serverless deployment.
Run this after deploying to Vercel to configure the webhook URL.
"""

import sys

import requests

from cryptoward.utils import Level, Settings, log


def set_webhook(webhook_url: str) -> None:
    """Set the webhook URL for the Telegram bot."""
    url = f"https://api.telegram.org/bot{Settings.TELEGRAM_BOT_TOKEN}/setWebhook"

    payload = {
        "url": webhook_url,
        "allowed_updates": ["message", "callback_query"],
    }

    log(f"Setting webhook to: {webhook_url}", Level.INFO)
    response = requests.post(url, json=payload, timeout=30)

    if response.status_code == 200:
        result = response.json()
        if result.get("ok"):
            log("✅ Webhook set successfully!", Level.INFO)
            log(f"Response: {result}", Level.DEBUG)
        else:
            log(f"❌ Failed to set webhook: {result}", Level.ERROR)
            sys.exit(1)
    else:
        log(f"❌ HTTP Error {response.status_code}: {response.text}", Level.ERROR)
        sys.exit(1)


def get_webhook_info() -> None:
    """Get current webhook information."""
    url = f"https://api.telegram.org/bot{Settings.TELEGRAM_BOT_TOKEN}/getWebhookInfo"

    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        result = response.json()
        if result.get("ok"):
            log("Current webhook info:", Level.INFO)
            log(f"{result.get('result')}", Level.INFO)
        else:
            log(f"Failed to get webhook info: {result}", Level.ERROR)
    else:
        log(f"HTTP Error {response.status_code}: {response.text}", Level.ERROR)


def delete_webhook() -> None:
    """Delete the current webhook."""
    url = f"https://api.telegram.org/bot{Settings.TELEGRAM_BOT_TOKEN}/deleteWebhook"

    response = requests.post(url, timeout=30)

    if response.status_code == 200:
        result = response.json()
        if result.get("ok"):
            log("✅ Webhook deleted successfully!", Level.INFO)
        else:
            log(f"❌ Failed to delete webhook: {result}", Level.ERROR)
    else:
        log(f"❌ HTTP Error {response.status_code}: {response.text}", Level.ERROR)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/set_webhook.py <webhook_url>  - Set webhook")
        print("  python scripts/set_webhook.py info            - Get webhook info")
        print("  python scripts/set_webhook.py delete          - Delete webhook")
        print()
        print("Example:")
        print("  python scripts/set_webhook.py https://your-app.vercel.app/api/webhook")
        sys.exit(1)

    command = sys.argv[1]

    if command == "info":
        get_webhook_info()
    elif command == "delete":
        delete_webhook()
    else:
        # Treat as webhook URL
        set_webhook(command)

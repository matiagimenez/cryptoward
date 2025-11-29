from telegram import BotCommand

WELCOME_MESSAGE = (
    "👋 Hi! I can send you daily crypto price updates.\n\n"
    "To set a schedule, use:\n"
    "/set <HH.MM>\n\n"
    "📝 Example: /set 09.30\n\n"
    "The time is in 24h format\n"
    "The timezone is UTC\n"
    "If you want to remove the schedule, use:\n"
    "/remove\n"
)

BOT_COMMANDS_DESCRIPTIONS = {
    BotCommand("start", "Start the bot and see welcome message"),
    BotCommand("set", "Set daily alert (e.g., /set 09.30)"),
    BotCommand("help", "Get usage instructions"),
    BotCommand("remove", "Remove daily alert"),
    BotCommand("clear", "Clear conversation history"),
}

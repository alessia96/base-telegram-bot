from dotenv import load_dotenv
import logging
import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters
)

from utils import process_message


logger = logging.getLogger(__name__)
logger.setLevel('INFO')

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_NAME = os.getenv('BOT_NAME')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user.first_name is not None else user.username
    welcome_msg = f"Welcome {name}! I'm {BOT_NAME}."

    await update.message.reply_text(welcome_msg)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user.first_name is not None else user.username
    help_text = f"Hi {name}! I'm {BOT_NAME} 😁 \nTo begin a conversation just write and send a message."
    await update.message.reply_text(help_text)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = process_message(text=update.message.text, username=update.effective_user.username)
    await update.message.reply_text(msg)


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND & ~filters.Entity('hashtag'), echo
        )
    )
    application.run_polling(allowed_updates=Update.ALL_TYPES)




if __name__ == "__main__":
    main()
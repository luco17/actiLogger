"""
Connect to Telegram bot
"""

import os
import logging
import boto3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TABLE=os.environ.get('TABLE')
TOKEN=os.environ.get('BOT_TOKEN')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s  %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send message when command/start is issued"""
    user = update.effective_user
    update.message.reply_text(
        (f"Hi {user.first_name} welcome to the activity bot. Press /log to"
        " record you activity"))


def log(update: Update, context: CallbackContext) -> None:
    """Log a user's response"""
    activity=context.args[0]
    duration=context.args[1]
    date=update.message.date.strftime('%Y-%m-%d')

    update.message.reply_text(f"{activity}: {duration}, {date}")

    table.put_item(
        Item={
        'activity': activity,
        'date': date,
        'minutes': duration})


def handler(event, context):
    

def main() -> None:
    """Start ze bot"""
    updater = Updater(TOKEN)
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("log", log))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    Application,
    filters,
    CallbackQueryHandler,
)
from Func import Func
import random
import time
from States import command_called,user_requests, user_info, RECEIVER_CHAT_ID,TOKEN
from Forwarders import forward_message ,user_requests,user_info
    
async def start(update: Update, context: CallbackContext) -> None:
        await update.message.reply_text('سلام من ربات پیشرو آتیه هستم با دستور /help میتونید لیست دستورات موجود رو ببینید')


async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Available Commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/req_buy - Recieves your request items and send it to Pishro HR\n"
        "/daily_leave - Send day off request\n"
        "/hourly_leave - send hourly leave request\n"
        "/overwork - Send overtime work request\n"
        "/work_mission - send work mission request\n"
        "/oncall - send oncall request"
    )
    await update.message.reply_text(help_text)

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


async def forward_message(update: Update, context: CallbackContext) -> None:
    chatid = update.message.chat_id
    username = update.message.from_user.username     
    user_id = update.message.from_user.id   
    messageid = update.message.message_id
    unique_id = int(Func.generate_unique_id(user_id))
    
    # Determine the type of request based on command flags.
    special_comment = ""
    if command_called["dl"]:
        special_comment = "مرخصی روزانه"
    elif command_called["hl"]:
        special_comment = "مرخصی ساعتی"
    elif command_called["ow"]:
        special_comment = "اضافه کاری"
    elif command_called["wm"]:
        special_comment = "ماموریت"
    elif command_called["rb"]:
        special_comment = "درخواست خرید"
    elif command_called["oc"]:
        special_comment = "درخواست دورکاری"
    
    full_message = (
        f"{unique_id}\n----------------------\n"
        f"type: {special_comment}\n"
        f"User: {username}\n"
        f"message: {update.message.text}\n"
    )
    
    # Try sending the complete message to HR, and make sure we capture the response.
    try:
        receiver_message = await context.bot.send_message(
            chat_id=RECEIVER_CHAT_ID, 
            text=full_message
        )
    except Exception as e:
        # Log the error if needed and notify the sender.
        await update.message.reply_text("ارسال پیام به HR با مشکل مواجه شد.")
        return

    # Now that we know send_message succeeded, we can safely get the message ID.
    receiver_message_id = receiver_message.message_id

    # Store both the original and the formatted message data.
    user_requests[unique_id] = { 
        "user_id": user_id,               
        "chat_id": chatid,
        "username": username,
        "message_id": messageid,         # Original user's message ID.
        "receiver_message_id": receiver_message_id  # Bot’s complete forwarded message ID.
    }    

    user_info[chatid] = {
        "user_message_id": messageid,
        "reciever_message_id": receiver_message_id
    }
    
    await update.message.reply_text('درخواست شما ارسال شد')
    
    
    for key in command_called:
        command_called[key] = False

        #---turn back to false

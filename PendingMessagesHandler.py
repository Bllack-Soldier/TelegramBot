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


async def req_list(update: Update, context: CallbackContext) -> None:
    if update.message.chat_id == int(RECEIVER_CHAT_ID):
        if not user_requests:
            await update.message.reply_text("هیچ درخواستی در صف وجود ندارد.")
            return

        keyboard = []
        for unique_id, req in user_requests.items():
            # Each button is labeled with the unique ID and the sender's username.
            button = InlineKeyboardButton(
                text=f"Req {unique_id}: {req.get('username', 'Unknown')}",
                callback_data=f"req_{unique_id}"
            )
            keyboard.append([button])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Select a request to re-forward the complete message:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text("شما مجاز به استفاده از این دستور نیستید.")

# Callback handler for inline button clicks.
async def req_button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data

    if data.startswith("req_"):
        try:
            unique_id = int(data.split("_")[1])
        except Exception:
            await query.answer("Invalid callback data", show_alert=True)
            return
        
        req = user_requests.get(unique_id)
        if req:
            # Instead of using original user message information, we now use
            # the forwarded (complete) message ID that the bot sent to HR.
            receiver_message_id = req.get("receiver_message_id")
            if receiver_message_id is not None:
                try:
                    # Use copy_message to re-send the complete message
                    # (the one with full details) into HR’s chat.
                    await context.bot.copy_message(
                        chat_id=update.effective_chat.id,  # HR chat
                        from_chat_id=RECEIVER_CHAT_ID,
                        message_id=receiver_message_id
                    )
                    await query.answer("پیام کامل مجدداً ارسال شد.")
                except Exception as e:
                    await query.answer("فوروارد کامل پیام با مشکل مواجه شد.", show_alert=True)
            else:
                await query.answer("اطلاعات پیام کامل موجود نیست.", show_alert=True)
        else:
            await query.answer("درخواست یافت نشد.", show_alert=True)

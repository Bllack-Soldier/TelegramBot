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





async def apply_req(update: Update, context: CallbackContext) -> None:
    if update.message.chat_id == int(RECEIVER_CHAT_ID):
        
        # Check if the received message is a reply
        if update.message.reply_to_message: 
            replied=update.message.reply_to_message.text
            original_user_id = int(replied.split()[0])
            
            response_message = update.message.text
            comm="درخواست شما تایید شد"
            # Send the response back to the original user
            if original_user_id in user_requests:
                user_id=user_requests[original_user_id]
                chat_id = user_requests[original_user_id]["chat_id"]
                message_id = user_requests[original_user_id]["message_id"]
                await context.bot.send_message(chat_id=chat_id, text=comm, reply_to_message_id=message_id)
                del user_requests[original_user_id]
                await update.message.reply_text(f'باقی مانده در صف:\n{Func.get_all_usernames(user_dict=user_requests)}\n')

                await update.message.reply_text("پاسخ ارسال شد.")
            else:
                await update.message.reply_text("کاربری یافت نشد.")
        else:
            await update.message.reply_text("لطفا پیام درخواست را ریپلای کنید.")
    else:
        await update.message.reply_text("شما مجاز به استفاده از این دستور نیستید.") 
                
#--------------------------

async def reject_req(update: Update, context: CallbackContext) -> None:
    if update.message.chat_id == int(RECEIVER_CHAT_ID):
        
        # Check if the received message is a reply
        if update.message.reply_to_message:
            replied=update.message.reply_to_message.text
            original_user_id = int(replied.split()[0])

            # Send the response back to the original user
            if original_user_id in user_requests:
                user_id=user_requests[original_user_id]
                chat_id = user_requests[original_user_id]["chat_id"]
                message_id = user_requests[original_user_id]["message_id"]
                comm="درخواست شما رد شد"
                await context.bot.send_message(chat_id=chat_id, text=comm, reply_to_message_id=message_id)
                #delete user req from queue after hr respond
                del user_requests[original_user_id]
                await update.message.reply_text(f'باقی مانده در صف:\n{Func.get_all_usernames(user_dict=user_requests)}\n')
                await update.message.reply_text("پاسخ ارسال شد.")
            else:
                await update.message.reply_text("کاربری یافت نشد.")
        else:
            await update.message.reply_text("لطفا پیام درخواست را ریپلای کنید.")
    else:
        await update.message.reply_text("شما مجاز به استفاده از این دستور نیستید.")


#--------------------------

  

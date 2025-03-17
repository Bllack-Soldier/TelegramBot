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







async def daily_leave(update: Update, context: CallbackContext) -> None:
    command_called["dl"] = True
    
    await update.message.reply_text("لطفا اطلاعات مورد نیاز را با فرمت زیر ارسال کنید")

    format = (
        "نام-نام خانوادگی:\n"
        "تاریخ شروع:\n"
        "تاریخ پایان:\n"
        "توضیحات:\n"
    )
    await update.message.reply_text(format)
        
        
    #-------------------------------------------------
async def hourly_leave(update: Update, context: CallbackContext) -> None:
    command_called["hl"] = True
    
    await update.message.reply_text('لطفا نام و نام خانوادگی خود را به همراه مدت مرخصی با فرمت زیراعلام کنید')
    
    format = (
        "نام-نام خانوادگی:\n"
        "تاریخ:\n"
        "ساعت شروع - پایان:\n"
        "توضیحات:\n"
    )
    await update.message.reply_text(format)
#-------------------------------------------------

async def req_buy(update: Update, context: CallbackContext) -> None:
    command_called["rb"] = True
    
    await update.message.reply_text('لطفا مشخصات اقلام مورد نیاز را طبق فرمت زیر وارد کنید')
    format = (
        "نام-نام خانوادگی:\n"
        "عنوان پروژه و نام شرکت:\n"
        "لیست اقلام مورد نیاز:\n"
        "(در صورت نیاز)توضیحات:\n"
    )
    await update.message.reply_text(format)

#-------------------------------------------------

async def overtime_work(update: Update, context: CallbackContext) -> None:
    command_called["ow"]= True
    
    await update.message.reply_text('لطفا درخواست اضافه کاری را طبق فرمت زیر ارسال کنید')
    format = (
        "نام-نام خانوادگی:\n"
        "تاریخ:\n"
        "ساعت شروع - پایان:\n"
        "توضیحات:\n"
    )
    await update.message.reply_text(format)

#-------------------------------------------------

async def work_mission(update: Update, context: CallbackContext) -> None:
    command_called["wm"]= True

    await update.message.reply_text('لطفا درخواست ماموریت را طبق فرمت زیر ارسال کنید')
    format = (
        "نام-نام خانوادگی:\n"
        "محل ماموریت:\n"
        "تاریخ:\n"
        "ساعت شروع - پایان:\n"
        "(در صورت نیاز)توضیحات:\n"
    )
    await update.message.reply_text(format)
    
#--------------------------
async def oncall(update: Update, context: CallbackContext) -> None:
    command_called["oc"]= True

    await update.message.reply_text('لطفا درخواست oncall را طبق فرمت زیر ارسال کنید')
    format = (
        "نام-نام خانوادگی:\n"
        "محل ماموریت:\n"
        "تاریخ:\n"
        "ساعت شروع - پایان:\n"
        "(در صورت نیاز)توضیحات:\n"
    )
    await update.message.reply_text(format)
    
#--------------------------    
async def overtime_work(update: Update, context: CallbackContext) -> None:
    command_called["ow"]= True
    
    await update.message.reply_text('لطفا درخواست اضافه کاری را طبق فرمت زیر ارسال کنید')
    format = (
        "نام-نام خانوادگی:\n"
        "تاریخ:\n"
        "ساعت شروع - پایان:\n"
        "توضیحات:\n"
    )
    await update.message.reply_text(format)
#--------------------------
    
async def delete_message(update: Update, context: CallbackContext) -> None:
    chat_id=update.message.chat_id   
    user_id=update.message.from_user.id
    if  update.message.reply_to_message:
        message_id=update.message.reply_to_message.message_id
        #when user send a req its user id maps with two attributes : users own message id and reciever message id
        # (for that specific request message) and that dictionary is use in this method to find message id and remove it
        reciever_message_id = user_info[chat_id]["reciever_message_id"]
        await context.bot.delete_message(chat_id=RECEIVER_CHAT_ID,message_id=reciever_message_id)
        await update.message.reply_text("درخواست ارسال شده حذف شد!")
        del user_info[chat_id]
        del user_requests[user_id]
    else:
        await update.message.reply_text("لطفا پیامی که قصد حذف آن را دارید ریپلای کنید")     


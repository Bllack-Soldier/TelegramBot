from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext,Application,filters
from Func import Func


TOKEN = '' #Token for accessing telegram API server
RECEIVER_CHAT_ID = '' 


#Flags
command_called = { 
    "dl":False,
    "hl":False,
    "rb":False,
    "ow":False,
    "wm":False,
    "oc":False
    }
#information gathering while user send request(for reciever usage)
user_requests = {}                              # <--- target of creation this dic is help reciever to send back response to senders

#information gathering while user send request and cache it (for user usage)
user_info={}                                    # <--- target of creation this dic is helping user when wants delete or edit sended message




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
#-------------------------------------------------
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
            
            response_message = update.message.text

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
async def req_list(update: Update, context: CallbackContext) -> None:
    if update.message.chat_id == int(RECEIVER_CHAT_ID):
        await update.message.reply_text(f'steel in queue:\n{Func.get_all_usernames(user_dict=user_requests)}\n')
    else : 
        await update.message.reply_text("شما مجاز به استفاده از این دستور نیستید.")
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
          
        
#--------------------------  




async def forward_message(update: Update, context: CallbackContext) -> None:
    #---
    chatid=update.message.chat_id
    username=update.message.from_user.username
    user_id=update.message.from_user.id
    messageid=update.message.message_id
    #---
    user_requests[user_id] = {                
        "chat_id": chatid,
        "username": username,
        "message_id": messageid
        }
    
    

    user_identifier=update.message.from_user.id
    user_id=update.message.from_user.username
    full_name = user_id
    message = update.message.text

    if command_called["dl"] == True:
        special_comment = "مرخصی روزانه"
    elif command_called["hl"] == True:
        special_comment = "مرخصی ساعتی"
    elif command_called["ow"] == True:
        special_comment = "اضافه کاری"
    elif command_called["wm"] == True:
        special_comment = "ماموریت"
    elif command_called["rb"] == True:
        special_comment = "درخواست خرید"
    elif command_called["oc"]== True:
        special_comment = "درخواست دورکاری"
    #######################    
    #excluded_command="test"
    
    #if  message.lower().startswith(excluded_command.lower()):
    #    await receiver_message_handler(update,context) 
    #######################
    full_message = f"{user_identifier}\n----------------------\ntype:{special_comment}\nUser: {full_name}\nmessage: {message}\n"
    receiver_message=await context.bot.send_message(chat_id=RECEIVER_CHAT_ID , text=full_message)
    messageid2=receiver_message.message_id

    user_info[chatid]={
        "user_message_id":messageid,
        "reciever_message_id":messageid2
    }

    await update.message.reply_text('درخواست شما ارسال شد')
    
    for key in command_called:
        command_called[key] = False

        #---turn back to false

 
        
    
    #---
    
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("req_buy", req_buy))
    application.add_handler(CommandHandler("overwork", overtime_work))
    application.add_handler(CommandHandler("work_mission", work_mission))
    application.add_handler(CommandHandler("hourly_leave", hourly_leave))
    application.add_handler(CommandHandler("daily_leave", daily_leave))
    application.add_handler(CommandHandler("daily_leave", daily_leave))
    application.add_handler(CommandHandler("req_list", req_list))
    application.add_handler(CommandHandler("apply_req", apply_req))
    application.add_handler(CommandHandler("reject_req", reject_req))
    application.add_handler(CommandHandler("oncall", oncall))
    application.add_handler(CommandHandler("delete_message", delete_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()

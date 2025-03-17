from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Application,
    filters,
    CallbackQueryHandler,
)
# Import your modules/functions and state.
from States import TOKEN
from Forwarders import forward_message
from PendingMessagesHandler import req_button_callback, req_list
from InfoHandlers import start, help_command
from WorkHandlers import daily_leave, hourly_leave, req_buy, overtime_work, work_mission, oncall, delete_message
from ManagerSideHandlers import apply_req, reject_req

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("req_buy", req_buy))
    application.add_handler(CommandHandler("overwork", overtime_work))
    application.add_handler(CommandHandler("work_mission", work_mission))
    application.add_handler(CommandHandler("hourly_leave", hourly_leave))
    application.add_handler(CommandHandler("daily_leave", daily_leave))
    application.add_handler(CommandHandler("req_list", req_list))
    application.add_handler(CommandHandler("apply_req", apply_req))
    application.add_handler(CommandHandler("reject_req", reject_req))
    application.add_handler(CommandHandler("oncall", oncall))
    application.add_handler(CommandHandler("delete_message", delete_message))
    
    # Register message and callback query handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    application.add_handler(CallbackQueryHandler(req_button_callback))
    
    application.run_polling()

if __name__ == '__main__':
    main()

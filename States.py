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
user_info={}  # <--- target of creation this dic is helping user when wants delete or edit sended message


TOKEN = 'YourOwnToken' #Token for accessing telegram API server
RECEIVER_CHAT_ID = '294690202' #in this case Pishronet.HR person #hr chat id is 171852929 #developer chat id is 294690202

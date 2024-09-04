this is the engine of a simple Telegram Bot written in python.
first install requirement libraries :
$pip install -r  requirements.txt


the skin of this engine will create by "https://t.me/BotFather" and commands can be define by this official telegram bot .
every command that exist in telegram bot should handle inside code .

functionality:
generally gets a message from user,gets his account attributes such as message id - chat id - user id  and forward the message to HR person 
and HR send response back to user by reply on users message and use one of apply or deny commands .
this engine is statefull and needs a database but i didn't attach a db on this project.
additional functions are written in a separate class(Func.py).

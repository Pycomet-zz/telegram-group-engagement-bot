from app import *

@bot.message_handler(commands=['start'])
def start(msg):
    
    bot.reply_to(
        msg,
        "Hi There"
    )


    
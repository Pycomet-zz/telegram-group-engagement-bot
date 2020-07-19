from app import *


keyboard = types.InlineKeyboardMarkup(row_width=1)
a = types.InlineKeyboardButton(text=emoji.emojize(":memo: Activate Subscriber", use_aliases=True), callback_data="activate")
b = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Send Advertisement", use_aliases=True), callback_data="ad")
c = types.InlineKeyboardButton(text=emoji.emojize(":memo: Deactivate Subscriber", use_aliases=True), callback_data="deactivate")
keyboard.add(a,c,b)


@bot.message_handler(commands=['admin', 'panel'])
def handle_admin(msg):
    """Admin feature to the bot management"""

    if msg.from_user.id == int(ADMIN_ID):

        bot.send_message(
            msg.chat.id,
            f"""
Welcome Back {msg.from_user.username},
            
    <b>Dx30 Group Administrative Panel.</b>""",
            reply_markup=keyboard,
            parse_mode=telegram.ParseMode.HTML
        )

    else:
        bot.reply_to(
            msg,
            "You are not authorized to use this command"
        )
from app import *


keyboard = types.InlineKeyboardMarkup(row_width=1)
a = types.InlineKeyboardButton(text=emoji.emojize(":memo: Activate Subscriber", use_aliases=True), callback_data="add_subscriber")
b = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Send Advert to Pod", use_aliases=True), callback_data="send_ad")
c = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Deactivate Subscriber", use_aliases=True), callback_data="remove_subscriber")
keyboard.add(a,b,c)


@bot.message_handler(commands=['admin', 'panel'])
def handle_admin(msg):
    """Admin feature to the bot management"""

    if msg.from_user.id == int(ADMIN_ID):

        bot.send_message(
            msg.chat.id,
            f"Hello {msg.from_user.username}, welcome back to the Dx15 bot administrative panel.",
            reply_markup=keyboard
        )

    else:
        bot.reply_to(
            msg,
            "You are not authorized to use this command"
        )